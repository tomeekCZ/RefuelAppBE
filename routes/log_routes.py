from flask import Blueprint, request, jsonify
from models.refuel_log import RefuelLog
from services.db import db

log_bp = Blueprint("log_bp", __name__, url_prefix="/api/logs")

@log_bp.route("/", methods=["GET"], strict_slashes=False)
def get_logs():
    logs = RefuelLog.query.all()
    return jsonify([log.to_dict() for log in logs])

# Get single log by ID
@log_bp.route("/<int:log_id>", methods=["GET"], strict_slashes=False)
def get_log(log_id):
    log = RefuelLog.query.get_or_404(log_id)
    return jsonify(log.to_dict()), 200

@log_bp.route("/", methods=["POST"], strict_slashes=False)
def create_log():
    data = request.json
    required = ["userId", "carId", "date", "mileage", "liters", "price", "currencyId"]
    if not all(data.get(k) for k in required):
        return jsonify({"error": "Missing required fields"}), 400

    log = RefuelLog(
        user_id=data["userId"],
        car_id=data["carId"],
        date=data["date"],
        mileage=data["mileage"],
        liters=data["liters"],
        price=data["price"],
        currency_id=data["currencyId"],
        station_brand=data.get("stationBrand"),
        comments=data.get("comments"),
        lat=data.get("lat"),
        lon=data.get("lon"),
    )
    db.session.add(log)
    db.session.commit()
    return jsonify(log.to_dict()), 201

@log_bp.route("/<int:log_id>", methods=["PUT"], strict_slashes=False)
def update_log(log_id):
    log = RefuelLog.query.get_or_404(log_id)
    data = request.json

    log.user_id = data.get("userId", log.user_id)
    log.car_id = data.get("carId", log.car_id)
    log.date = data.get("date", log.date)
    log.mileage = data.get("mileage", log.mileage)
    log.liters = data.get("liters", log.liters)
    log.price = data.get("price", log.price)
    log.currency_id = data.get("currencyId", log.currency_id)
    log.station_brand = data.get("stationBrand", log.station_brand)
    log.comments = data.get("comments", log.comments)
    log.lat = data.get("lat", log.lat)
    log.lon = data.get("lon", log.lon)

    db.session.commit()
    return jsonify(log.to_dict()), 200



@log_bp.route("/<int:log_id>", methods=["DELETE"], strict_slashes=False)
def delete_log(log_id):
    log = RefuelLog.query.get_or_404(log_id)
    db.session.delete(log)
    db.session.commit()
    return jsonify({"message": "Log deleted"}), 200
