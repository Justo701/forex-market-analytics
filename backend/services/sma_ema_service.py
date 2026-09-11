"""
SMA and EMA service.

This module prepares Simple Moving Average (SMA)
and Exponential Moving Average (EMA) data
for the API layer.
"""

from backend.repositories.sma_ema_repository import get_sma_ema


# ============================================================
# GET SMA AND EMA DATA
# ============================================================

def get_sma_ema_data():
    """
    Retrieve and prepare SMA and EMA data.

    Returns:
        A list of SMA and EMA dictionaries.
    """

    rows = get_sma_ema()

    sma_ema_data = []

    for row in rows:

        analysis = {
            "trade_date": str(row["trade_date"]),
            "pair": row["pair"],

            "close_price": float(
                row["close_price"]
            ),

            "sma_3": float(
                row["sma_3"]
            ),

            "sma_5": float(
                row["sma_5"]
            ),

            "ema_3": float(
                row["ema_3"]
            ),

            "ema_5": float(
                row["ema_5"]
            )
        }

        sma_ema_data.append(analysis)

    return sma_ema_data
