"""
Indicator combinations service.

This module prepares combined indicator data
for the API layer.
"""

from backend.repositories.indicator_combinations_repository import (
    get_indicator_combinations
)


def get_indicator_combinations_data():
    """
    Retrieve and prepare combined indicator data.

    Returns:
        A list of indicator combination dictionaries.
    """

    rows = get_indicator_combinations()

    combination_data = []

    for row in rows:

        analysis = {
            "trade_date": str(row["trade_date"]),
            "pair": row["pair"],
            "close_price": float(row["close_price"]),

            "ema_3": (
                float(row["ema_3"])
                if row["ema_3"] is not None
                else None
            ),

            "ema_5": (
                float(row["ema_5"])
                if row["ema_5"] is not None
                else None
            ),

            "rsi_14": (
                float(row["rsi_14"])
                if row["rsi_14"] is not None
                else None
            ),

            "trend": row["trend"],
            "momentum": row["momentum"],
            "confirmation": row["confirmation"]
        }

        combination_data.append(analysis)

    return combination_data
