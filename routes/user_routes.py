from flask import Blueprint, request, jsonify
from models.users import User
from services.db import db
from werkzeug.security import generate_password_hash

user_bp = Blueprint("user_bp", __name__, url_prefix="/api/users")

@user_bp.route("/", methods=["GET"], strict_slashes=False)
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@user_bp.route("/<int:user_id>", methods=["GET"], strict_slashes=False)
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

@user_bp.route("/", methods=["POST"], strict_slashes=False)
def create_user():
    data = request.json
    required_fields = ["username", "email", "password"]
    if not all(data.get(field) for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "Username already exists"}), 400

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Email already exists"}), 400

    hashed_password = generate_password_hash(data["password"])
    user = User(
        username=data["username"],
        email=data["email"],
        display_name=data.get("displayName", ""),
        password=hashed_password,
        preferred_currency_id=data.get("preferredCurrencyId"),
        primary_car_id=data.get("primaryCarId"),
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@user_bp.route("/<int:user_id>", methods=["PUT"], strict_slashes=False)
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json

    user.username = data.get("username", user.username)
    user.email = data.get("email", user.email)
    user.display_name = data.get("displayName", user.display_name)
    user.primary_car_id = data.get("primaryCarId", user.primary_car_id)
    user.preferred_currency_id = data.get("preferredCurrencyId", user.preferred_currency_id)
    
    if "password" in data and data["password"]:
        user.password = generate_password_hash(data["password"])

    db.session.commit()
    return jsonify(user.to_dict()), 200