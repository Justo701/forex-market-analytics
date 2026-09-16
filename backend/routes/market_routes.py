from flask import Blueprint, jsonify

market_bp = Blueprint("market", __name__)


@market_bp.route("/api/status")
def status():
    return jsonify({
        "application": "Forex Market Analytics",
        "message": "API is operational",
        "status": "running"
    })
