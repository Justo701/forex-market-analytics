"""
Forex Market Analytics API.

A Flask-based backend application that provides API endpoints
for application status, Forex prices, and price movement analysis.
"""

from flask import Flask, jsonify
import mariadb


# ============================================================
# IMPORT APPLICATION COMPONENTS
# ============================================================

# Price repository
#
# Responsible for retrieving Forex price data
# from MariaDB.
from backend.services.price_service import get_price_data

# Movement service
#
# Responsible for retrieving and preparing
# Forex movement analysis.
#
# The service internally communicates with:
#
#     movement_repository.py
#
# We therefore do NOT import the movement repository directly here.
from backend.services.movement_service import get_movement_analysis


# ============================================================
# CREATE THE FLASK APPLICATION
# ============================================================

app = Flask(__name__)


# ============================================================
# ROUTE 1: HOME
# ============================================================

@app.route("/")
def home():
    """
    Return the API welcome message.
    """

    return "Forex Market Analytics API"


# ============================================================
# ROUTE 2: API STATUS
# ============================================================

@app.route("/api/status")
def status():
    """
    Return the current API status.
    """

    return jsonify({
        "application": "Forex Market Analytics",
        "status": "running",
        "message": "API is operational"
    })


# ============================================================
# ROUTE 3: FOREX PRICES
# ============================================================

@app.route("/api/prices")
def prices():
    """
    Return Forex price data as JSON.
    """

    try:

        # Ask the service for prepared price data.
        price_data = get_price_data()

        # Return the data as JSON.
        return jsonify(price_data)

    except mariadb.Error as error:

        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500

# ============================================================
# ROUTE 4: PRICE MOVEMENTS
# ============================================================

@app.route("/api/movements")
def movements():
    """
    Retrieve Forex price movement analysis
    and return it as JSON.

    Flow:

        Client
          ↓
        Flask route
          ↓
        Movement service
          ↓
        Movement repository
          ↓
        MariaDB
          ↓
        Movement analysis
          ↓
        JSON response
    """

    try:

        # ----------------------------------------------------
        # GET MOVEMENT ANALYSIS FROM THE SERVICE
        # ----------------------------------------------------

        # The service handles the application-level
        # preparation of the movement data.
        movement_data = get_movement_analysis()


        # ----------------------------------------------------
        # RETURN JSON RESPONSE
        # ----------------------------------------------------

        return jsonify(movement_data)


    except mariadb.Error as error:

        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500


# ============================================================
# START DEVELOPMENT SERVER
# ============================================================

if __name__ == "__main__":

    # Start Flask's development server.
    #
    # debug=True allows Flask to automatically reload
    # when we change the code during development.
    #
    # Do NOT use debug=True in production.
    app.run(debug=True)
