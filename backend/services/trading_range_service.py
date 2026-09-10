"""
Trading range service.

This module prepares Forex trading range
analysis for the API layer.
"""

from backend.repositories.trading_range_repository import (
    get_trading_range_analysis
)


# ============================================================
# GET TRADING RANGE DATA
# ============================================================

def get_trading_range_data():
    """
    Retrieve and prepare Forex trading range data.

    Returns:
        A list of trading range dictionaries.
    """

    rows = get_trading_range_analysis()

    trading_range_data = []

    for row in rows:

        analysis = {
            "trade_date": row["trade_date"].isoformat(),
            "pair": row["pair"],
            "close_price": float(row["close_price"]),

            "range_high": float(row["range_high"]),

            "range_low": float(row["range_low"]),

            "range_size": float(row["range_size"]),

            "range_position_percentage": (
                float(row["range_position_percentage"])
                if row["range_position_percentage"] is not None
                else None
            )
        }

        trading_range_data.append(analysis)

    return trading_range_data
