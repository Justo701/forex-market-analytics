"""
Multi-pair comparison service.

This module prepares comparative Forex pair
analysis for the API layer.
"""

from backend.repositories.multi_pair_comparison_repository import (
    get_multi_pair_comparison
)


# ============================================================
# GET MULTI-PAIR COMPARISON DATA
# ============================================================

def get_multi_pair_comparison_data():
    """
    Retrieve and prepare multi-pair comparison data.

    Returns:
        A list of multi-pair comparison dictionaries.
    """

    rows = get_multi_pair_comparison()

    comparison_data = []

    for row in rows:

        analysis = {
            "pair": row["pair"],

            "average_price": float(
                row["average_price"]
            ),

            "highest_price": float(
                row["highest_price"]
            ),

            "lowest_price": float(
                row["lowest_price"]
            ),

            "average_daily_movement": float(
                row["average_daily_movement"]
            ),

            "price_volatility": float(
                row["price_volatility"]
            )
        }

        comparison_data.append(analysis)

    return comparison_data
