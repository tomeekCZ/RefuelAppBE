from flask import Flask
from flask_cors import CORS, cross_origin
from services.db import db
from routes import register_routes
from errors import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    register_routes(app)
    register_error_handlers(app)

    # Enable CORS for all routes
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8000)
