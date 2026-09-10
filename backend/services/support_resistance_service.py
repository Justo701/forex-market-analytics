"""
Support and resistance service.

This module prepares support and resistance data
for the API layer.
"""

from backend.repositories.support_resistance_repository import (
    get_support_resistance_analysis
)


# ============================================================
# GET SUPPORT AND RESISTANCE DATA
# ============================================================

def get_support_resistance_data():
    """
    Retrieve and prepare support and resistance data.

    Returns:
        A list of support and resistance dictionaries.
    """

    rows = get_support_resistance_analysis()

    support_resistance_data = []

    for row in rows:

        analysis = {
            "trade_date": row["trade_date"].isoformat(),
            "pair": row["pair"],
            "close_price": float(row["close_price"]),

            "previous_close": (
                float(row["previous_close"])
                if row["previous_close"] is not None
                else None
            ),

            "next_close": (
                float(row["next_close"])
                if row["next_close"] is not None
                else None
            ),

            "price_level": row["price_level"]
        }

        support_resistance_data.append(analysis)

    return support_resistance_data
