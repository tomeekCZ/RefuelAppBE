from flask import Blueprint, request, jsonify
from models.users import User
from services.db import db
from werkzeug.security import check_password_hash

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/login", methods=["POST"], strict_slashes=False)
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing JSON data"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return jsonify(user.to_dict())
    else:
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify(user.to_dict()), 200
