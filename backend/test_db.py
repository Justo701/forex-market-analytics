# ============================================================
# FOREX MARKET ANALYTICS
# MariaDB Data Retrieval Test
# ============================================================

import mariadb


try:

    # --------------------------------------------------------
    # STEP 1: CONNECT TO THE DATABASE
    # --------------------------------------------------------

    connection = mariadb.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="forex_market_analytics"
    )

    print("Database connection successful!")


    # --------------------------------------------------------
    # STEP 2: CREATE A CURSOR
    # --------------------------------------------------------

    # A cursor allows Python to send SQL commands
    # to the database and read the results.
    cursor = connection.cursor()


    # --------------------------------------------------------
    # STEP 3: EXECUTE SQL
    # --------------------------------------------------------

    cursor.execute("""
        SELECT
            trade_date,
            pair,
            close_price
        FROM forex_prices
        ORDER BY trade_date;
    """)


    # --------------------------------------------------------
    # STEP 4: READ THE RESULTS
    # --------------------------------------------------------

    rows = cursor.fetchall()


    # --------------------------------------------------------
    # STEP 5: DISPLAY THE RESULTS
    # --------------------------------------------------------

    print("\nForex prices:")

    for row in rows:
        print(row)


# ------------------------------------------------------------
# HANDLE DATABASE ERRORS
# ------------------------------------------------------------

except mariadb.Error as error:

    print(f"Database error: {error}")


# ------------------------------------------------------------
# CLOSE DATABASE RESOURCES
# ------------------------------------------------------------

else:

    cursor.close()
    connection.close()

    print("\nDatabase connection closed.")
