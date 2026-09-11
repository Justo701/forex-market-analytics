"""
RSI repository.

This module retrieves 14-period RSI analysis
from the MariaDB database.
"""

from backend.config.database import get_db_connection


# ============================================================
# GET RSI DATA
# ============================================================

def get_rsi():
    """
    Retrieve 14-period RSI calculations.

    Returns:
        A list of database rows.
    """

    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            WITH price_changes AS (

                SELECT
                    trade_date,
                    pair,
                    close_price,

                    LAG(close_price) OVER (
                        PARTITION BY pair
                        ORDER BY trade_date
                    ) AS previous_close

                FROM forex_prices
            ),

            changes AS (

                SELECT
                    trade_date,
                    pair,
                    close_price,

                    close_price - previous_close
                        AS price_change,

                    CASE
                        WHEN close_price - previous_close > 0
                        THEN close_price - previous_close
                        ELSE 0
                    END AS gain,

                    CASE
                        WHEN close_price - previous_close < 0
                        THEN previous_close - close_price
                        ELSE 0
                    END AS loss

                FROM price_changes
            ),

            rsi_calculation AS (

                SELECT
                    trade_date,
                    pair,
                    close_price,

                    AVG(gain) OVER (
                        PARTITION BY pair
                        ORDER BY trade_date
                        ROWS BETWEEN 13 PRECEDING
                        AND CURRENT ROW
                    ) AS average_gain,

                    AVG(loss) OVER (
                        PARTITION BY pair
                        ORDER BY trade_date
                        ROWS BETWEEN 13 PRECEDING
                        AND CURRENT ROW
                    ) AS average_loss

                FROM changes
            )

            SELECT
                trade_date,
                pair,
                close_price,

                ROUND(average_gain, 5)
                    AS average_gain,

                ROUND(average_loss, 5)
                    AS average_loss,

                ROUND(
                    average_gain /
                    NULLIF(average_loss, 0),
                    5
                ) AS relative_strength,

                ROUND(
                    100 - (
                        100 / (
                            1 +
                            (
                                average_gain /
                                NULLIF(average_loss, 0)
                            )
                        )
                    ),
                    5
                ) AS rsi_14

            FROM rsi_calculation

            ORDER BY
                pair,
                trade_date;
        """)

        rows = cursor.fetchall()

        return rows

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
