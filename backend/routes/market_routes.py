from flask import Blueprint, jsonify

from backend.services.price_service import get_price_data
from backend.services.movement_service import get_movement_analysis
from backend.services.crossover_service import get_crossover_analysis_data
from backend.services.support_resistance_service import get_support_resistance_data
from backend.services.trend_analysis_service import get_trend_analysis_data
from backend.services.price_momentum_service import get_price_momentum_data
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


# ============================================================
# MARKET BLUEPRINT
# ============================================================

market_bp = Blueprint("market", __name__)


# ============================================================
# API STATUS
# ============================================================

@market_bp.route("/api/status")
def status():
    """
    Return the current API status.
    """

    return jsonify({
        "application": "Forex Market Analytics",
        "message": "API is operational",
        "status": "running"
    })


# ============================================================
# PRICE DATA
# ============================================================

@market_bp.route("/api/prices")
def prices():
    """
    Return Forex price data.
    """

    price_data = get_price_data()

    return jsonify(price_data)


# ============================================================
# PRICE MOVEMENTS
# ============================================================

@market_bp.route("/api/movements")
def movements():
    """
    Return Forex price movement analysis.
    """

    movement_data = get_movement_analysis()

    return jsonify(movement_data)


# ============================================================
# MOVING-AVERAGE CROSSOVERS
# ============================================================

@market_bp.route("/api/crossovers")
def crossover_analysis():
    """
    Return moving-average crossover analysis.
    """

    crossover_data = get_crossover_analysis_data()

    return jsonify(crossover_data)


# ============================================================
# SUPPORT AND RESISTANCE
# ============================================================

@market_bp.route("/api/support-resistance")
def support_resistance_analysis():
    """
    Return support and resistance analysis.
    """

    data = get_support_resistance_data()

    return jsonify(data)


# ============================================================
# TREND ANALYSIS
# ============================================================

@market_bp.route("/api/trends")
def trend_analysis():
    """
    Return Forex trend analysis.
    """

    data = get_trend_analysis_data()

    return jsonify(data)


# ============================================================
# PRICE MOMENTUM
# ============================================================

@market_bp.route("/api/momentum")
def price_momentum():
    """
    Return Forex price momentum analysis.
    """

    data = get_price_momentum_data()

    return jsonify(data)


# ============================================================
# TRADING RANGE
# ============================================================

@market_bp.route("/api/trading-range")
def trading_range():
    """
    Return Forex trading-range analysis.
    """

    data = get_trading_range_data()

    return jsonify(data)


# ============================================================
# ADVANCED VOLATILITY
# ============================================================

@market_bp.route("/api/advanced-volatility")
def advanced_volatility():
    """
    Return advanced Forex volatility analysis.
    """

    data = get_advanced_volatility_data()

    return jsonify(data)


# ============================================================
# RISK CLASSIFICATION
# ============================================================

@market_bp.route("/api/risk-classification")
def risk_classification():
    """
    Return Forex risk classification.
    """

    data = get_risk_classification_data()

    return jsonify(data)


# ============================================================
# MULTI-PAIR COMPARISON
# ============================================================

@market_bp.route("/api/multi-pair-comparison")
def multi_pair_comparison():
    """
    Return multi-pair Forex comparison.
    """

    data = get_multi_pair_comparison_data()

    return jsonify(data)


# ============================================================
# SMA / EMA
# ============================================================

@market_bp.route("/api/sma-ema")
def sma_ema():
    """
    Return SMA and EMA analysis.
    """

    data = get_sma_ema_data()

    return jsonify(data)


# ============================================================
# RSI
# ============================================================

@market_bp.route("/api/rsi")
def rsi():
    """
    Return RSI analysis.
    """

    data = get_rsi_data()

    return jsonify(data)


# ============================================================
# MACD
# ============================================================

@market_bp.route("/api/macd")
def macd():
    """
    Return MACD analysis.
    """

    data = get_macd_data()

    return jsonify(data)


# ============================================================
# BOLLINGER BANDS
# ============================================================

@market_bp.route("/api/bollinger-bands")
def bollinger_bands():
    """
    Return Bollinger Bands analysis.
    """

    data = get_bollinger_bands_data()

    return jsonify(data)


# ============================================================
# ATR
# ============================================================

@market_bp.route("/api/atr")
def atr():
    """
    Return Average True Range analysis.
    """

    data = get_atr_data()

    return jsonify(data)


# ============================================================
# INDICATOR COMBINATIONS
# ============================================================

@market_bp.route("/api/indicator-combinations")
def indicator_combinations():
    """
    Return combined technical-indicator analysis.
    """

    data = get_indicator_combinations_data()

    return jsonify(data)
