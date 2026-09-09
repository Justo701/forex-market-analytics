"""
Market statistics repository.

This module is responsible for retrieving
market statistics from MariaDB.
"""

from backend.config.database import get_db_connection


def get_market_statistics():
    """
    Retrieve basic market statistics from MariaDB.

    Returns:
        A list of database rows.
    """

    connection = None
    cursor = None

    try:

        # Connect to MariaDB using values from .env.
        connection = get_db_connection()

        cursor = connection.cursor(dictionary = True)

        # Execute the market statistics query.
        cursor.execute("""
            SELECT
                pair,
                ROUND(AVG(close_price), 5) AS average_price,
                ROUND(MAX(close_price), 5) AS highest_price,
                ROUND(MIN(close_price), 5) AS lowest_price,
                COUNT(*) AS total_records
            FROM forex_prices
            GROUP BY pair;
        """)

        # Get the rows returned by MariaDB.
        rows = cursor.fetchall()

        # Return raw database rows.
        return rows

    finally:

        # Close the cursor.
        if cursor is not None:
            cursor.close()

        # Close the database connection.
        if connection is not None:
            connection.close()
