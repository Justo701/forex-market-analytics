"""
Advanced volatility repository.

This module retrieves rolling Forex volatility
analysis from the MariaDB database.
"""

from backend.config.database import get_db_connection


# ============================================================
# GET ADVANCED VOLATILITY ANALYSIS
# ============================================================

def get_advanced_volatility_analysis():
    """
    Retrieve rolling Forex volatility analysis.

    The query calculates:

    - Previous closing price
    - Daily percentage change
    - 5-period rolling volatility

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

            percentage_changes AS (

                SELECT
                    trade_date,
                    pair,
                    close_price,
                    previous_close,

                    (
                        (close_price - previous_close)
                        / previous_close
                    ) * 100 AS percentage_change

                FROM price_changes
            ),

            rolling_volatility AS (

                SELECT
                    trade_date,
                    pair,
                    close_price,
                    percentage_change,

                    STDDEV(percentage_change) OVER (
                        PARTITION BY pair
                        ORDER BY trade_date
                        ROWS BETWEEN 4 PRECEDING
                        AND CURRENT ROW
                    ) AS volatility

                FROM percentage_changes
            )

            SELECT
                trade_date,
                pair,
                close_price,

                ROUND(
                    percentage_change,
                    5
                ) AS percentage_change,

                ROUND(
                    volatility,
                    5
                ) AS rolling_volatility

            FROM rolling_volatility

            ORDER BY pair, trade_date;
        """)

        rows = cursor.fetchall()

        return rows

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
