"""
Trend analysis repository.

This module retrieves Forex trend analysis
from the MariaDB database.
"""

from backend.config.database import get_db_connection


# ============================================================
# GET TREND ANALYSIS
# ============================================================

def get_trend_analysis():
    """
    Retrieve Forex trend analysis.

    The query calculates:

    - Previous closing price
    - 3-period moving average
    - 5-period moving average
    - Trend classification

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
            WITH price_analysis AS (

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

            moving_averages AS (

                SELECT
                    trade_date,
                    pair,
                    close_price,
                    previous_close,

                    AVG(close_price) OVER (
                        PARTITION BY pair
                        ORDER BY trade_date
                        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
                    ) AS ma_3,

                    AVG(close_price) OVER (
                        PARTITION BY pair
                        ORDER BY trade_date
                        ROWS BETWEEN 4 PRECEDING AND CURRENT ROW
                    ) AS ma_5

                FROM price_analysis
            )

            SELECT
                trade_date,
                pair,
                close_price,

                ROUND(previous_close, 5)
                    AS previous_close,

                ROUND(ma_3, 5)
                    AS ma_3,

                ROUND(ma_5, 5)
                    AS ma_5,

                CASE

                    WHEN close_price > previous_close
                         AND ma_3 > ma_5
                        THEN 'Uptrend'

                    WHEN close_price < previous_close
                         AND ma_3 < ma_5
                        THEN 'Downtrend'

                    ELSE 'Sideways'

                END AS trend

            FROM moving_averages

            ORDER BY pair, trade_date;
        """)

        rows = cursor.fetchall()
        return rows

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
