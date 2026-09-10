"""
Trend analysis service.

This module prepares Forex trend analysis
for the API layer.
"""

from backend.repositories.trend_analysis_repository import (
    get_trend_analysis
)


# ============================================================
# GET TREND ANALYSIS DATA
# ============================================================

def get_trend_analysis_data():
    """
    Retrieve and prepare Forex trend analysis.

    Returns:
        A list of trend analysis dictionaries.
    """

    rows = get_trend_analysis()

    trend_data = []

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

            "ma_3": float(row["ma_3"]),
            "ma_5": float(row["ma_5"]),
            "trend": row["trend"]
        }

        trend_data.append(analysis)

    return trend_data
