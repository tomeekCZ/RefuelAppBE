from flask import jsonify, request
import logging
import traceback

# Configure logger to write to stderr
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        logger.warning(f"404 Not Found: {request.path}")
        return jsonify({"error": "Not found", "message": str(error)}), 404

    @app.errorhandler(400)
    def bad_request(error):
        logger.warning(f"400 Bad Request: {request.path}")
        return jsonify({"error": "Bad request", "message": str(error)}), 400

    @app.errorhandler(500)
    def internal_server_error(error):
        logger.error(f"500 Internal Server Error: {request.path}")
        logger.error(traceback.format_exc())
        return jsonify({"error": "Internal server error", "message": str(error)}), 500

    @app.errorhandler(Exception)
    def handle_exception(error):
        logger.error(f"Unexpected Exception at {request.path}: {error}")
        logger.error(traceback.format_exc())
        return jsonify({"error": "Unexpected error", "message": str(error)}), 500
