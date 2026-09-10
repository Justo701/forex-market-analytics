"""
Advanced volatility service.

This module prepares rolling Forex volatility
analysis for the API layer.
"""

from backend.repositories.advanced_volatility_repository import (
    get_advanced_volatility_analysis
)


# ============================================================
# GET ADVANCED VOLATILITY DATA
# ============================================================

def get_advanced_volatility_data():
    """
    Retrieve and prepare advanced volatility data.

    Returns:
        A list of advanced volatility dictionaries.
    """

    rows = get_advanced_volatility_analysis()

    volatility_data = []

    for row in rows:

        analysis = {
            "trade_date": row["trade_date"].isoformat(),
            "pair": row["pair"],
            "close_price": float(row["close_price"]),

            "percentage_change": (
                float(row["percentage_change"])
                if row["percentage_change"] is not None
                else None
            ),

            "rolling_volatility": (
                float(row["rolling_volatility"])
                if row["rolling_volatility"] is not None
                else None
            )
        }

        volatility_data.append(analysis)

    return volatility_data
