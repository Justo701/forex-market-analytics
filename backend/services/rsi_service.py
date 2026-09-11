from backend.repositories.rsi_repository import get_rsi
def get_rsi_data():
    """
    Retrieve and prepare RSI data.

    Returns:
        A list of RSI dictionaries.
    """

    rows = get_rsi()

    rsi_data = []

    for row in rows:

        analysis = {
            "trade_date": str(row["trade_date"]),
            "pair": row["pair"],
            "close_price": float(row["close_price"]),

            "average_gain": (
                float(row["average_gain"])
                if row["average_gain"] is not None
                else None
            ),

            "average_loss": (
                float(row["average_loss"])
                if row["average_loss"] is not None
                else None
            ),

            "relative_strength": (
                float(row["relative_strength"])
                if row["relative_strength"] is not None
                else None
            ),

            "rsi_14": (
                float(row["rsi_14"])
                if row["rsi_14"] is not None
                else None
            )
        }

        rsi_data.append(analysis)

    return rsi_data
