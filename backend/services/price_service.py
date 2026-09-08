"""
Price service.

This module contains application logic
for Forex price data.
"""

# Import the repository function.
#
# The service does NOT connect directly to MariaDB.
# It asks the repository to provide the data.
from backend.repositories.price_repository import get_all_prices


def get_price_data():
    """
    Get Forex prices from the repository
    and prepare them for the application.
    """

    # --------------------------------------------------------
    # STEP 1: GET DATA FROM REPOSITORY
    # --------------------------------------------------------

    rows = get_all_prices()

    # At this point rows might look like:
    #
    # [
    #     (2026-01-01, 'EURUSD', 1.101),
    #     (2026-01-02, 'EURUSD', 1.104),
    #     ...
    # ]

    # --------------------------------------------------------
    # STEP 2: PREPARE APPLICATION DATA
    # --------------------------------------------------------

    price_data = []

    for row in rows:

        price = {
            "trade_date": row[0].isoformat(),
            "pair": row[1],
            "close_price": float(row[2])
        }

        price_data.append(price)

    # --------------------------------------------------------
    # STEP 3: RETURN PREPARED DATA
    # --------------------------------------------------------

    return price_data
