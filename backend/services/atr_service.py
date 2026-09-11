"""
ATR service.

This module prepares ATR data
for the API layer.
"""

from backend.repositories.atr_repository import get_atr


def get_atr_data():
    """
    Retrieve and prepare ATR data.

    Returns:
        A list of ATR dictionaries.
    """

    rows = get_atr()

    atr_data = []

    for row in rows:

        analysis = {
            "trade_date": str(row["trade_date"]),
            "pair": row["pair"],
            "close_price": float(row["close_price"]),

            "true_range": (
                float(row["true_range"])
                if row["true_range"] is not None
                else None
            ),

            "atr_14": (
                float(row["atr_14"])
                if row["atr_14"] is not None
                else None
            )
        }

        atr_data.append(analysis)

    return atr_data
