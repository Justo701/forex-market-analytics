"""
ATR repository.

This module retrieves ATR data
from the MariaDB database.
"""

from backend.config.database import get_db_connection


def get_atr():
    """
    Retrieve ATR data from the database.

    Returns:
        A list of ATR database rows.
    """

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        query = """
        WITH price_data AS (

            SELECT
                trade_date,
                pair,
                high_price,
                low_price,
                close_price,

                LAG(close_price) OVER (
                    PARTITION BY pair
                    ORDER BY trade_date
                ) AS previous_close

            FROM forex_prices
        ),

        true_range AS (

            SELECT
                trade_date,
                pair,
                high_price,
                low_price,
                close_price,
                previous_close,

                GREATEST(
                    high_price - low_price,

                    ABS(
                        high_price - previous_close
                    ),

                    ABS(
                        low_price - previous_close
                    )
                ) AS true_range

            FROM price_data
        ),

        atr_calculation AS (

            SELECT
                trade_date,
                pair,
                close_price,
                true_range,

                COUNT(true_range) OVER (
                    PARTITION BY pair
                    ORDER BY trade_date
                    ROWS BETWEEN 13 PRECEDING AND CURRENT ROW
                ) AS period_count,

                AVG(true_range) OVER (
                    PARTITION BY pair
                    ORDER BY trade_date
                    ROWS BETWEEN 13 PRECEDING AND CURRENT ROW
                ) AS atr_14

            FROM true_range
        )

        SELECT
            trade_date,
            pair,
            close_price,

            ROUND(true_range, 5) AS true_range,

            ROUND(
                CASE
                    WHEN period_count = 14
                    THEN atr_14
                    ELSE NULL
                END,
                5
            ) AS atr_14

        FROM atr_calculation

        ORDER BY
            pair,
            trade_date
        """

        cursor.execute(query)

        return cursor.fetchall()

    finally:

        cursor.close()
        connection.close()
