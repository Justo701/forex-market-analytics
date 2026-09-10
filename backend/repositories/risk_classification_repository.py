"""
Risk classification repository.

This module retrieves Forex risk classification
analysis from the MariaDB database.
"""

from backend.config.database import get_db_connection


# ============================================================
# GET RISK CLASSIFICATION
# ============================================================

def get_risk_classification():
    """
    Retrieve Forex risk classification analysis.

    The query calculates:

    - Daily percentage change
    - 5-period rolling volatility
    - Average volatility
    - Risk level

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
                    ) AS rolling_volatility

                FROM percentage_changes
            ),

            volatility_average AS (

                SELECT
                    trade_date,
                    pair,
                    close_price,
                    percentage_change,
                    rolling_volatility,

                    AVG(rolling_volatility) OVER (
                        PARTITION BY pair
                    ) AS average_volatility

                FROM rolling_volatility
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
                    rolling_volatility,
                    5
                ) AS rolling_volatility,

                ROUND(
                    average_volatility,
                    5
                ) AS average_volatility,

                CASE

                    WHEN rolling_volatility IS NULL
                        THEN 'Unknown'

                    WHEN rolling_volatility < average_volatility
                        THEN 'Low Risk'

                    WHEN rolling_volatility > average_volatility
                        THEN 'High Risk'

                    ELSE 'Moderate Risk'

                END AS risk_level

            FROM volatility_average

            ORDER BY pair, trade_date;
        """)

        rows = cursor.fetchall()

        return rows

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
