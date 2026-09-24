"""
Forex Market Analytics API.

Flask application entry point.
Routes are organized using Flask Blueprints.
"""
from flask_cors import CORS
from flask import Flask

from backend.routes.market_routes import market_bp
import mariadb
from backend.errors.handlers import handle_database_error

# ============================================================
# APPLICATION FACTORY
# ============================================================

def create_app():
    """
    Create and configure the Flask application.
    """

    app = Flask(__name__)
    CORS(app)
    app.register_error_handler(mariadb.Error, handle_database_error)

    # Register the market API routes.
    app.register_blueprint(market_bp)

    # ========================================================
    # HOME ROUTE
    # ========================================================

    @app.route("/")
    def home():
        """
        Return the API welcome message.
        """

        return "Forex Market Analytics API"

    return app


# ============================================================
# DEVELOPMENT SERVER
# ============================================================

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
