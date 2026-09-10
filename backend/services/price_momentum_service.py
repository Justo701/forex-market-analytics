"""
Price momentum service.

This module prepares Forex price momentum
analysis for the API layer.
"""

from backend.repositories.price_momentum_repository import (
    get_price_momentum_analysis
)


# ============================================================
# GET PRICE MOMENTUM DATA
# ============================================================

def get_price_momentum_data():
    """
    Retrieve and prepare Forex price momentum data.

    Returns:
        A list of price momentum dictionaries.
    """

    rows = get_price_momentum_analysis()

    momentum_data = []

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

            "momentum": (
                float(row["momentum"])
                if row["momentum"] is not None
                else None
            ),

            "momentum_percentage": (
                float(row["momentum_percentage"])
                if row["momentum_percentage"] is not None
                else None
            ),

            "momentum_status": row["momentum_status"]
        }

        momentum_data.append(analysis)

    return momentum_data
