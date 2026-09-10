"""
Price momentum repository.

This module retrieves Forex price momentum
analysis from the MariaDB database.
"""

from backend.config.database import get_db_connection


# ============================================================
# GET PRICE MOMENTUM ANALYSIS
# ============================================================

def get_price_momentum_analysis():
    """
    Retrieve Forex price momentum analysis.

    The query calculates:

    - Previous closing price
    - Price momentum
    - Momentum percentage
    - Momentum status

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
            )

            SELECT
                trade_date,
                pair,
                close_price,

                ROUND(previous_close, 5)
                    AS previous_close,

                ROUND(
                    close_price - previous_close,
                    5
                ) AS momentum,

                ROUND(
                    (
                        (close_price - previous_close)
                        / previous_close
                    ) * 100,
                    5
                ) AS momentum_percentage,

                CASE

                    WHEN close_price > previous_close
                        THEN 'Positive'

                    WHEN close_price < previous_close
                        THEN 'Negative'

                    ELSE 'Neutral'

                END AS momentum_status

            FROM price_analysis

            ORDER BY pair, trade_date;
        """)

        rows = cursor.fetchall()

        return rows

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
