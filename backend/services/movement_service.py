"""
Movement service.

This module contains business logic related to
Forex price movement analysis.
"""

from backend.repositories.movement_repository import get_movements


# ============================================================
# GET MOVEMENT ANALYSIS
# ============================================================

def get_movement_analysis():
    """
    Retrieve Forex movement analysis.

    The repository is responsible for getting the data
    from MariaDB.

    The service is responsible for preparing the data
    for the application.

    Returns:
        A list of movement dictionaries.
    """

    # --------------------------------------------------------
    # GET DATA FROM REPOSITORY
    # --------------------------------------------------------

    rows = get_movements()


    # --------------------------------------------------------
    # CONVERT DATABASE ROWS INTO APPLICATION DATA
    # --------------------------------------------------------

    movement_data = []

    for row in rows:

        movement = {
    "trade_date": row["trade_date"].isoformat(),
    "pair": row["pair"],
    "close_price": float(row["close_price"]),

    "previous_close": (
        float(row["previous_close"])
        if row["previous_close"] is not None
        else None
    ),

    "price_change": (
        float(row["price_change"])
        if row["price_change"] is not None
        else None
    ),

    "percentage_change": (
        float(row["percentage_change"])
        if row["percentage_change"] is not None
        else None
    ),

    "absolute_percentage_change": (
        float(row["absolute_percentage_change"])
        if row["absolute_percentage_change"] is not None
        else None
    ),

    "movement_class": row["movement_class"]
}
        movement_data.append(movement)


    # --------------------------------------------------------
    # RETURN APPLICATION DATA
    # --------------------------------------------------------

    return movement_data
