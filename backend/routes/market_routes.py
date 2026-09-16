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
from backend.services.crossover_service import get_crossover_analysis_data


@market_bp.route("/api/crossovers", methods=["GET"])
def crossover_analysis():
    """
    Retrieve moving-average crossover analysis
    and return it as JSON.
    """

    try:
        # Ask the service for crossover analysis.
        crossover_data = get_crossover_analysis_data()

        # Return the result as JSON.
        return jsonify(crossover_data)

    except mariadb.Error as error:

        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
from backend.services.support_resistance_service import get_support_resistance_data


@market_bp.route("/api/support-resistance", methods=["GET"])
def support_resistance_analysis():
    """
    Retrieve support and resistance analysis
    and return it as JSON.
    """

    try:
        # Ask the service for support and resistance analysis.
        support_resistance_data = get_support_resistance_data()

        # Return the result as JSON.
        return jsonify(support_resistance_data)

    except mariadb.Error as error:

        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
from backend.services.trend_analysis_service import get_trend_analysis_data


@market_bp.route("/api/trends", methods=["GET"])
def trend_analysis():
    """
    Retrieve Forex trend analysis
    and return it as JSON.
    """

    try:
        # Ask the service for trend analysis.
        trend_data = get_trend_analysis_data()

        # Return the result as JSON.
        return jsonify(trend_data)

    except mariadb.Error as error:

        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
