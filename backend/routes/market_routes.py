from flask import Blueprint, jsonify
import mariadb
from backend.services.price_service import get_price_data
from backend.services.movement_service import get_movement_analysis

market_bp = Blueprint("market", __name__)


@market_bp.route("/api/status")
def status():
    return jsonify({
        "application": "Forex Market Analytics",
        "message": "API is operational",
        "status": "running"
    })


@market_bp.route("/api/prices")
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
@market_bp.route("/api/movements")
def movements():
    """
    Retrieve Forex price movement analysis
    and return it as JSON.
    """

    try:
        # Ask the service to prepare the movement analysis.
        movement_data = get_movement_analysis()

        # Return the prepared data as JSON.
        return jsonify(movement_data)

    except mariadb.Error as error:

        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
