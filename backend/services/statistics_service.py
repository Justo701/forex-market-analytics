"""
Market statistics service.

This module contains application logic for
market statistics.
"""

from backend.repositories.statistics_repository import (
    get_market_statistics
)


def get_market_statistics_data():
    """
    Get market statistics from the repository
    and prepare them for the application.

    Returns:
        A list of market statistics dictionaries.
    """

    # Ask the Repository to retrieve the data.
    rows = get_market_statistics()

    # This list will contain the data prepared
    # for the application.
    statistics_data = []

    # Process each database row.
    for row in rows:

        statistics = {
            "pair": row[0],
            "average_price": float(row[1]),
            "highest_price": float(row[2]),
            "lowest_price": float(row[3]),
            "total_records": row[4]
        }

        # Add the prepared dictionary to our list.
        statistics_data.append(statistics)

    # Return the prepared data.
    return statistics_data
