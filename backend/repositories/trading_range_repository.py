"""
Trading range repository.

This module retrieves Forex trading range
analysis from the MariaDB database.
"""

from backend.config.database import get_db_connection


# ============================================================
# GET TRADING RANGE ANALYSIS
# ============================================================

def get_trading_range_analysis():
    """
    Retrieve Forex trading range analysis.

    The query calculates:

    - Rolling 5-period high
    - Rolling 5-period low
    - Trading range size
    - Current price position within the range

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
            WITH trading_ranges AS (

                SELECT
                    trade_date,
                    pair,
                    close_price,

                    MAX(close_price) OVER (
                        PARTITION BY pair
                        ORDER BY trade_date
                        ROWS BETWEEN 4 PRECEDING
                        AND CURRENT ROW
                    ) AS range_high,

                    MIN(close_price) OVER (
                        PARTITION BY pair
                        ORDER BY trade_date
                        ROWS BETWEEN 4 PRECEDING
                        AND CURRENT ROW
                    ) AS range_low

                FROM forex_prices
            )

            SELECT
                trade_date,
                pair,
                close_price,

                ROUND(range_high, 5)
                    AS range_high,

                ROUND(range_low, 5)
                    AS range_low,

                ROUND(
                    range_high - range_low,
                    5
                ) AS range_size,

                ROUND(
                    (
                        (close_price - range_low)
                        / NULLIF(range_high - range_low, 0)
                    ) * 100,
                    2
                ) AS range_position_percentage

            FROM trading_ranges

            ORDER BY pair, trade_date;
        """)

        rows = cursor.fetchall()

        return rows

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
