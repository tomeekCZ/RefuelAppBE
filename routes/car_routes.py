from flask import Blueprint, request, jsonify
from models.car import Car
from services.db import db

car_bp = Blueprint("car_bp", __name__)

@car_bp.route("/", methods=["GET"], strict_slashes=False)
def get_all_cars():
    cars = Car.query.all()
    return jsonify([car.to_dict() for car in cars])

@car_bp.route("/", methods=["POST"], strict_slashes=False)
def create_car():
    data = request.json
    required_fields = ["brand", "model", "fuelType", "vin", "licencePlate"]
    if not all(data.get(f) for f in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    car = Car(
        brand=data["brand"],
        model=data["model"],
        vin=data.get("vin"),
        color=data.get("color"),
        fuel_type=data["fuelType"],
        description=data.get("description"),
        licence_plate=data.get("licencePlate")
    )
    db.session.add(car)
    db.session.commit()
    return jsonify(car.to_dict()), 201

@car_bp.route("/<int:car_id>", methods=["PUT"], strict_slashes=False)
def update_car(car_id):
    car = Car.query.get_or_404(car_id)
    data = request.json

    car.brand = data.get("brand", car.brand)
    car.model = data.get("model", car.model)
    car.vin = data.get("vin", car.vin)
    car.color = data.get("color", car.color)
    car.fuel_type = data.get("fuelType", car.fuel_type)
    car.description = data.get("description", car.description)
    car.is_archived = data.get("isArchived", car.is_archived)
    car.licence_plate = data.get("licencePlate", car.licence_plate)

    db.session.commit()
    return jsonify(car.to_dict()), 200

@car_bp.route("/<int:car_id>/archive", methods=["POST"], strict_slashes=False)
def archive_car(car_id):
    car = Car.query.get_or_404(car_id)
    car.is_archived = True
    db.session.commit()
    return jsonify({"message": "Car archived"})