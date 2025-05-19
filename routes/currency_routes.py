from flask import Blueprint, jsonify
from models.currency import Currency

currency_bp = Blueprint("currency_bp", __name__)

@currency_bp.route("/", methods=["GET"], strict_slashes=False)
def get_currencies():
    currencies = Currency.query.all()
    return jsonify([c.to_dict() for c in currencies])
