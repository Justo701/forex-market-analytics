"""
MACD repository.

This module retrieves MACD data
from the MariaDB database.
"""

from backend.config.database import get_db_connection


def get_macd():
    """
    Retrieve MACD data from the database.

    Returns:
        A list of MACD database rows.
    """

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        query = """
        WITH RECURSIVE price_data AS (

            SELECT
                trade_date,
                pair,
                close_price,

                ROW_NUMBER() OVER (
                    PARTITION BY pair
                    ORDER BY trade_date
                ) AS rn

            FROM forex_prices
        ),

        ema_calculation AS (

            SELECT
                trade_date,
                pair,
                close_price,
                rn,

                close_price AS ema_12,
                close_price AS ema_26

            FROM price_data

            WHERE rn = 1

            UNION ALL

            SELECT
                p.trade_date,
                p.pair,
                p.close_price,
                p.rn,

                (
                    (p.close_price * (2.0 / 13))
                    +
                    (e.ema_12 * (1 - 2.0 / 13))
                ) AS ema_12,

                (
                    (p.close_price * (2.0 / 27))
                    +
                    (e.ema_26 * (1 - 2.0 / 27))
                ) AS ema_26

            FROM ema_calculation AS e

            JOIN price_data AS p
                ON p.pair = e.pair
                AND p.rn = e.rn + 1
        ),

        macd_calculation AS (

            SELECT
                trade_date,
                pair,
                close_price,
                rn,
                ema_12,
                ema_26,

                ema_12 - ema_26 AS macd

            FROM ema_calculation
        )

        SELECT
            trade_date,
            pair,
            close_price,

            ROUND(ema_12, 5) AS ema_12,

            ROUND(ema_26, 5) AS ema_26,

            ROUND(
                CASE
                    WHEN rn >= 26
                    THEN macd
                    ELSE NULL
                END,
                5
            ) AS macd

        FROM macd_calculation

        ORDER BY
            pair,
            trade_date
        """

        cursor.execute(query)

        return cursor.fetchall()

    finally:

        cursor.close()
        connection.close()
