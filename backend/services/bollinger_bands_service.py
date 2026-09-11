"""
Bollinger Bands service.

This module prepares Bollinger Bands data
for the API layer.
"""

from backend.repositories.bollinger_bands_repository import (
    get_bollinger_bands
)


def get_bollinger_bands_data():
    """
    Retrieve and prepare Bollinger Bands data.

    Returns:
        A list of Bollinger Bands dictionaries.
    """

    rows = get_bollinger_bands()

    bollinger_data = []

    for row in rows:

        analysis = {
            "trade_date": str(row["trade_date"]),
            "pair": row["pair"],
            "close_price": float(row["close_price"]),

            "middle_band": (
                float(row["middle_band"])
                if row["middle_band"] is not None
                else None
            ),

            "upper_band": (
                float(row["upper_band"])
                if row["upper_band"] is not None
                else None
            ),

            "lower_band": (
                float(row["lower_band"])
                if row["lower_band"] is not None
                else None
            )
        }

        bollinger_data.append(analysis)

    return bollinger_data
