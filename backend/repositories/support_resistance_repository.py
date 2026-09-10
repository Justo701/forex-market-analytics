"""
Support and resistance repository.

This module retrieves support and resistance analysis
from the MariaDB database.
"""

from backend.config.database import get_db_connection


# ============================================================
# GET SUPPORT AND RESISTANCE ANALYSIS
# ============================================================

def get_support_resistance_analysis():
    """
    Retrieve support and resistance analysis.

    The query identifies:

    - Local highs as resistance
    - Local lows as support
    - Previous closing price
    - Next closing price

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
            WITH price_levels AS (

                SELECT
                    trade_date,
                    pair,
                    close_price,

                    LAG(close_price) OVER (
                        PARTITION BY pair
                        ORDER BY trade_date
                    ) AS previous_close,

                    LEAD(close_price) OVER (
                        PARTITION BY pair
                        ORDER BY trade_date
                    ) AS next_close

                FROM forex_prices
            )

            SELECT
                trade_date,
                pair,
                close_price,

                ROUND(previous_close, 5)
                    AS previous_close,

                ROUND(next_close, 5)
                    AS next_close,

                CASE

                    WHEN close_price > previous_close
                         AND close_price > next_close
                        THEN 'Resistance'

                    WHEN close_price < previous_close
                         AND close_price < next_close
                        THEN 'Support'

                    ELSE 'No Level'

                END AS price_level

            FROM price_levels

            ORDER BY pair, trade_date;
        """)

        rows = cursor.fetchall()
        return rows

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
