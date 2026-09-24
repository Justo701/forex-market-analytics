from flask import jsonify
import mariadb
def handle_database_error(error):
    return jsonify({
        "error": "Database error",
        "message": str(error)
    }), 500
