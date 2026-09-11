"""
Forex Market Analytics API.

A Flask-based backend application that provides API endpoints
for application status, Forex prices, price movement analysis,
and market statistics.
"""


# ============================================================
# IMPORTS
# ============================================================

from flask import Flask, jsonify
import mariadb

# Price service
#
# Responsible for retrieving and preparing
# Forex price data.
from backend.services.price_service import get_price_data

# Movement service
#
# Responsible for retrieving and preparing
# Forex movement analysis.
from backend.services.movement_service import get_movement_analysis

# Market statistics service
#
# Responsible for retrieving and preparing
# Forex market statistics.
from backend.services.statistics_service import (
    get_market_statistics_data
)
from backend.services.crossover_service import (
    get_crossover_analysis_data
)
from backend.services.support_resistance_service import (
    get_support_resistance_data
)
from backend.services.trend_analysis_service import (
    get_trend_analysis_data
)
from backend.services.price_momentum_service import (
    get_price_momentum_data
)
from backend.services.trading_range_service import (
    get_trading_range_data
)
from backend.services.advanced_volatility_service import (
    get_advanced_volatility_data
)
from backend.services.risk_classification_service import (
    get_risk_classification_data
)
from backend.services.multi_pair_comparison_service import (
    get_multi_pair_comparison_data
)
from backend.services.sma_ema_service import get_sma_ema_data
from backend.services.rsi_service import get_rsi_data
from backend.services.macd_service import get_macd_data
from backend.services.bollinger_bands_service import get_bollinger_bands_data
from backend.services.atr_service import get_atr_data
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
# ROUTE 5: MARKET STATISTICS
# ============================================================

@app.route("/api/statistics")
def statistics():
    """
    Retrieve Forex market statistics
    and return them as JSON.

    Flow:

        Client
          ↓
        Flask route
          ↓
        Statistics service
          ↓
        Statistics repository
          ↓
        MariaDB
          ↓
        Market statistics
          ↓
        JSON response
    """

    try:

        # ----------------------------------------------------
        # GET MARKET STATISTICS FROM THE SERVICE
        # ----------------------------------------------------

        # The service retrieves the statistics from
        # the repository and prepares the data.
        statistics_data = get_market_statistics_data()


        # ----------------------------------------------------
        # RETURN JSON RESPONSE
        # ----------------------------------------------------

        return jsonify(statistics_data)

    except mariadb.Error as error:

        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
# ============================================================
# ROUTE 6: MOVING-AVERAGE CROSSOVERS
# ============================================================

@app.route("/api/crossovers", methods=["GET"])
def crossover_analysis():
    """
    Retrieve moving-average crossover analysis
    and return it as JSON.

    Flow:

        Client
          ↓
        Flask route
          ↓
        Crossover service
          ↓
        Crossover repository
          ↓
        MariaDB
          ↓
        Crossover analysis
          ↓
        JSON response
    """

    try:

        # ----------------------------------------------------
        # GET CROSSOVER ANALYSIS FROM THE SERVICE
        # ----------------------------------------------------

        crossover_data = get_crossover_analysis_data()


        # ----------------------------------------------------
        # RETURN JSON RESPONSE
        # ----------------------------------------------------

        return jsonify(crossover_data)

    except mariadb.Error as error:

        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
# ============================================================
# ROUTE 7: SUPPORT AND RESISTANCE
# ============================================================

@app.route("/api/support-resistance", methods=["GET"])
def support_resistance_analysis():
    """
    Retrieve support and resistance analysis
    and return it as JSON.
    """

    try:

        support_resistance_data = get_support_resistance_data()

        return jsonify(support_resistance_data)

    except mariadb.Error as error:

        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
# ============================================================
# ROUTE 8: TREND ANALYSIS
# ============================================================

@app.route("/api/trends", methods=["GET"])
def trend_analysis():
    """
    Retrieve Forex trend analysis
    and return it as JSON.
    """

    try:

        trend_data = get_trend_analysis_data()

        return jsonify(trend_data)

    except mariadb.Error as error:

        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
# ============================================================
# ROUTE 9: PRICE MOMENTUM
# ============================================================

@app.route("/api/momentum", methods=["GET"])
def price_momentum():
    """
    Retrieve Forex price momentum
    and return it as JSON.
    """

    try:

        momentum_data = get_price_momentum_data()

        return jsonify(momentum_data)

    except mariadb.Error as error:

        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
 # ============================================================
# ROUTE 10: TRADING RANGE
# ============================================================

@app.route("/api/trading-range", methods=["GET"])
def trading_range():
    """
    Retrieve Forex trading range
    and return it as JSON.
    """

    try:

        trading_range_data = get_trading_range_data()

        return jsonify(trading_range_data)

    except mariadb.Error as error:

        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500   
 # ============================================================
# ROUTE 11: ADVANCED VOLATILITY
# ============================================================

@app.route("/api/advanced-volatility", methods=["GET"])
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
 # ============================================================
# RISK CLASSIFICATION ENDPOINT
# ============================================================

@app.route("/api/risk-classification")
def risk_classification():

    try:
        data = get_risk_classification_data()

        return jsonify(data)

    except mariadb.Error as error:

        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
# ============================================================
# MULTI-PAIR COMPARISON ENDPOINT
# ============================================================

@app.route("/api/multi-pair-comparison")
def multi_pair_comparison():

    try:
        data = get_multi_pair_comparison_data()

        return jsonify(data)

    except mariadb.Error as error:

        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
# ============================================================
# SMA AND EMA ENDPOINT
# ============================================================

@app.route("/api/sma-ema")
def sma_ema():

    try:
        data = get_sma_ema_data()

        return jsonify(data)

    except mariadb.Error as error:

        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
# ============================================================
# RSI ENDPOINT
# ============================================================

@app.route("/api/rsi")
def rsi():

    try:
        data = get_rsi_data()

        return jsonify(data)

    except mariadb.Error as error:

        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
# ============================================================
# MACD ENDPOINT
# ============================================================

@app.route("/api/macd")
def macd():

    try:
        data = get_macd_data()

        return jsonify(data)

    except mariadb.Error as error:

        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
# ============================================================
# BOLLINGER BANDS ENDPOINT
# ============================================================

@app.route("/api/bollinger-bands")
def bollinger_bands():

    try:
        data = get_bollinger_bands_data()

        return jsonify(data)

    except mariadb.Error as error:

        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500
# ============================================================
# ATR ENDPOINT
# ============================================================

@app.route("/api/atr")
def atr():

    try:
        data = get_atr_data()

        return jsonify(data)

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
