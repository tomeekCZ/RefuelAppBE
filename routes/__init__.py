from .auth_routes import auth_bp
from .car_routes import car_bp
from .log_routes import log_bp
from .user_routes import user_bp
from .currency_routes import currency_bp

def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(car_bp, url_prefix="/api/cars")
    app.register_blueprint(log_bp, url_prefix="/api/logs")
    app.register_blueprint(currency_bp, url_prefix="/api/currencies")