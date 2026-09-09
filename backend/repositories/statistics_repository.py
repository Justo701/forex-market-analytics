"""
Market statistics repository.

This module is responsible for retrieving
market statistics from MariaDB.
"""

import mariadb
import os

from dotenv import load_dotenv


# Load variables from the .env file.
load_dotenv()


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
        connection = mariadb.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        cursor = connection.cursor()

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
