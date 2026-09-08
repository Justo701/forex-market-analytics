"""
Movement repository.

This module retrieves Forex price movement analysis
from the MariaDB database.
"""

import mariadb


# ============================================================
# GET PRICE MOVEMENT ANALYSIS
# ============================================================

def get_movements():
    """
    Retrieve Forex price movement analysis.

    The query calculates:

    - Previous closing price
    - Price change
    - Percentage change
    - Absolute percentage change
    - Movement classification

    Returns:
        A list of database rows.

    Raises:
        mariadb.Error:
            If a database operation fails.
    """

    connection = None
    cursor = None

    try:

        # ----------------------------------------------------
        # CONNECT TO MARIA DB
        # ----------------------------------------------------

        connection = mariadb.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="",
            database="forex_market_analytics"
        )


        # ----------------------------------------------------
        # CREATE CURSOR
        # ----------------------------------------------------

        cursor = connection.cursor()


        # ----------------------------------------------------
        # EXECUTE MOVEMENT ANALYSIS QUERY
        # ----------------------------------------------------

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

            movement_analysis AS (

                SELECT
                    trade_date,
                    pair,
                    close_price,
                    previous_close,

                    close_price - previous_close
                        AS price_change,

                    (
                        (close_price - previous_close)
                        / previous_close
                    ) * 100
                        AS percentage_change,

                    ABS(
                        (
                            (close_price - previous_close)
                            / previous_close
                        ) * 100
                    )
                        AS absolute_percentage_change

                FROM price_analysis
            )

            SELECT
                trade_date,
                pair,
                close_price,

                ROUND(previous_close, 5)
                    AS previous_close,

                ROUND(price_change, 5)
                    AS price_change,

                ROUND(percentage_change, 5)
                    AS percentage_change,

                ROUND(absolute_percentage_change, 5)
                    AS absolute_percentage_change,

                CASE

                    WHEN absolute_percentage_change < 0.10
                        THEN 'Low Movement'

                    WHEN absolute_percentage_change <= 0.30
                        THEN 'Moderate Movement'

                    ELSE 'High Movement'

                END AS movement_class

            FROM movement_analysis

            ORDER BY pair, trade_date;
        """)


        # ----------------------------------------------------
        # GET RESULTS
        # ----------------------------------------------------

        rows = cursor.fetchall()

        return rows


    finally:

        # ----------------------------------------------------
        # CLOSE DATABASE RESOURCES
        # ----------------------------------------------------

        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
