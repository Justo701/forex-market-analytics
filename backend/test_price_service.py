"""
Test the price service.

This test checks whether the service can:
1. Get data from the repository.
2. Prepare the data.
3. Return the prepared data.
"""

from backend.services.price_service import get_price_data


# Call the service.
prices = get_price_data()


# Display the result.
for price in prices:
    print(price)
