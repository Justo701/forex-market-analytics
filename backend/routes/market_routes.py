from flask import Blueprint, jsonify
import mariadb
from backend.services.price_service import get_price_data
from backend.services.movement_service import get_movement_analysis
from backend.services.trading_range_service import get_trading_range_data
from backend.services.advanced_volatility_service import get_advanced_volatility_data
from backend.services.risk_classification_service import get_risk_classification_data
from backend.services.multi_pair_comparison_service import get_multi_pair_comparison_data
from backend.services.sma_ema_service import get_sma_ema_data
from backend.services.rsi_service import get_rsi_data
from backend.services.macd_service import get_macd_data
from backend.services.bollinger_bands_service import get_bollinger_bands_data
from backend.services.atr_service import get_atr_data
from backend.services.indicator_combinations_service import get_indicator_combinations_data
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
from backend.services.price_momentum_service import get_price_momentum_data


@market_bp.route("/api/momentum", methods=["GET"])
def price_momentum():
    """
    Retrieve Forex price momentum
    and return it as JSON.
    """

    try:
        # Ask the service for price momentum analysis.
        momentum_data = get_price_momentum_data()

        # Return the result as JSON.
        return jsonify(momentum_data)

    except mariadb.Error as error:

        return jsonify({
            "error": "Database error",
            "message": str(error) }), 500
@market_bp.route("/api/advanced-volatility", methods=["GET"])
def advanced_volatility():
    """
    Retrieve advanced Forex volatility
    and return it as JSON.
    """
    try:
        volatility_data = get_advanced_volatility_data()
        return jsonify(volatility_data)

    except mariadb.Error as error:
        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
@market_bp.route("/api/risk-classification")
def risk_classification():
    try:
        data = get_risk_classification_data()
        return jsonify(data)

    except mariadb.Error as error:
        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
@market_bp.route("/api/multi-pair-comparison")
def multi_pair_comparison():
    try:
        data = get_multi_pair_comparison_data()
        return jsonify(data)

    except mariadb.Error as error:
        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
@market_bp.route("/api/sma-ema")
def sma_ema():
    try:
        data = get_sma_ema_data()
        return jsonify(data)

    except mariadb.Error as error:
        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
@market_bp.route("/api/rsi")
def rsi():
    try:
        data = get_rsi_data()
        return jsonify(data)

    except mariadb.Error as error:
        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
@market_bp.route("/api/macd")
def macd():
    try:
        data = get_macd_data()
        return jsonify(data)
    except mariadb.Error as error:
        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
@market_bp.route("/api/bollinger-bands")
def bollinger_bands():
    try:
        data = get_bollinger_bands_data()
        return jsonify(data)
    except mariadb.Error as error:
        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
@market_bp.route("/api/atr")
def atr():
    try:
        data = get_atr_data()
        return jsonify(data)
    except mariadb.Error as error:
        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
@market_bp.route("/api/indicator-combinations")
def indicator_combinations():
    try:
        data = get_indicator_combinations_data()
        return jsonify(data)
    except mariadb.Error as error:
        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
