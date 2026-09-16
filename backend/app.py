"""
Forex Market Analytics API.

Flask application entry point.
Routes are organized using Flask Blueprints.
"""

from flask import Flask

from backend.routes.market_routes import market_bp


# ============================================================
# APPLICATION FACTORY
# ============================================================

def create_app():
    """
    Create and configure the Flask application.
    """

    app = Flask(__name__)

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
    app.run(debug=True)
