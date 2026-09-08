"""
Price repository.

This module is responsible for communicating with MariaDB
and retrieving Forex price data.
"""

import mariadb


# ============================================================
# GET ALL FOREX PRICES
# ============================================================

def get_all_prices():
    """
    Retrieve all Forex prices from the database.

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
        # CREATE DATABASE CURSOR
        # ----------------------------------------------------

        cursor = connection.cursor()

        # ----------------------------------------------------
        # EXECUTE SQL QUERY
        # ----------------------------------------------------

        cursor.execute("""
            SELECT
                trade_date,
                pair,
                close_price
            FROM forex_prices
            ORDER BY trade_date;
        """)

        # ----------------------------------------------------
        # RETRIEVE RESULTS
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
