"""
Moving-average crossover service.

This module prepares moving-average crossover data
for the API layer.
"""

from backend.repositories.crossover_repository import (
    get_crossover_analysis
)


# ============================================================
# GET CROSSOVER ANALYSIS DATA
# ============================================================

def get_crossover_analysis_data():
    """
    Retrieve and prepare moving-average crossover data.

    Returns:
        A list of crossover analysis dictionaries.
    """

    rows = get_crossover_analysis()

    crossover_data = []

    for row in rows:

        analysis = {
            "trade_date": row["trade_date"].isoformat(),
            "pair": row["pair"],
            "close_price": float(row["close_price"]),
            "ma_3": float(row["ma_3"]),
            "ma_5": float(row["ma_5"]),
            "trend_relationship": row["trend_relationship"],
            "previous_relationship": row["previous_relationship"],
            "crossover_signal": row["crossover_signal"]
        }

        crossover_data.append(analysis)

    return crossover_data
