"""
Risk classification service.

This module prepares Forex risk classification
data for the API layer.
"""

from backend.repositories.risk_classification_repository import (
    get_risk_classification
)


# ============================================================
# GET RISK CLASSIFICATION DATA
# ============================================================

def get_risk_classification_data():
    """
    Retrieve and prepare Forex risk classification data.

    Returns:
        A list of risk classification dictionaries.
    """

    rows = get_risk_classification()

    risk_data = []

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
            ),

            "average_volatility": (
                float(row["average_volatility"])
                if row["average_volatility"] is not None
                else None
            ),

            "risk_level": row["risk_level"]
        }

        risk_data.append(analysis)

    return risk_data
