"""
SMA and EMA repository.

This module retrieves Simple Moving Average (SMA)
and Exponential Moving Average (EMA) analysis
from the MariaDB database.
"""

from backend.config.database import get_db_connection


# ============================================================
# GET SMA AND EMA DATA
# ============================================================

def get_sma_ema():
    """
    Retrieve SMA and EMA calculations from the database.

    Returns:
        A list of database rows.

    Raises:
        mariadb.Error:
            If a database operation fails.
    """

    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
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

                -- Anchor
                SELECT
                    trade_date,
                    pair,
                    close_price,
                    rn,

                    close_price AS ema_3,
                    close_price AS ema_5

                FROM price_data

                WHERE rn = 1


                UNION ALL


                -- Recursive member
                SELECT
                    p.trade_date,
                    p.pair,
                    p.close_price,
                    p.rn,

                    (
                        (p.close_price * 0.5)
                        +
                        (e.ema_3 * 0.5)
                    ) AS ema_3,

                    (
                        (p.close_price * 0.3333333333)
                        +
                        (e.ema_5 * 0.6666666667)
                    ) AS ema_5

                FROM ema_calculation AS e

                JOIN price_data AS p
                    ON p.pair = e.pair
                    AND p.rn = e.rn + 1
            )

            SELECT
                e.trade_date,
                e.pair,
                e.close_price,

                ROUND(
                    AVG(e.close_price) OVER (
                        PARTITION BY e.pair
                        ORDER BY e.trade_date
                        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
                    ),
                    5
                ) AS sma_3,

                ROUND(
                    AVG(e.close_price) OVER (
                        PARTITION BY e.pair
                        ORDER BY e.trade_date
                        ROWS BETWEEN 4 PRECEDING AND CURRENT ROW
                    ),
                    5
                ) AS sma_5,

                ROUND(e.ema_3, 5) AS ema_3,

                ROUND(e.ema_5, 5) AS ema_5

            FROM ema_calculation AS e

            ORDER BY
                e.pair,
                e.trade_date;
        """)

        rows = cursor.fetchall()

        return rows

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
