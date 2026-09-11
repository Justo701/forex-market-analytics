"""
MACD service.

This module prepares MACD data
for the API layer.
"""

from backend.repositories.macd_repository import get_macd


def get_macd_data():
    """
    Retrieve and prepare MACD data.

    Returns:
        A list of MACD dictionaries.
    """

    rows = get_macd()

    macd_data = []

    for row in rows:

        analysis = {
            "trade_date": str(row["trade_date"]),
            "pair": row["pair"],
            "close_price": float(row["close_price"]),

            "ema_12": (
                float(row["ema_12"])
                if row["ema_12"] is not None
                else None
            ),

            "ema_26": (
                float(row["ema_26"])
                if row["ema_26"] is not None
                else None
            ),

            "macd": (
                float(row["macd"])
                if row["macd"] is not None
                else None
            )
        }

        macd_data.append(analysis)

    return macd_data
