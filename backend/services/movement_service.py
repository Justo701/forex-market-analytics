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
            "trade_date": row[0].isoformat(),

            "pair": row[1],

            "close_price": float(row[2]),

            "previous_close": (
                float(row[3])
                if row[3] is not None
                else None
            ),

            "price_change": (
                float(row[4])
                if row[4] is not None
                else None
            ),

            "percentage_change": (
                float(row[5])
                if row[5] is not None
                else None
            ),

            "absolute_percentage_change": (
                float(row[6])
                if row[6] is not None
                else None
            ),

            "movement_class": row[7]
        }

        movement_data.append(movement)


    # --------------------------------------------------------
    # RETURN APPLICATION DATA
    # --------------------------------------------------------

    return movement_data
