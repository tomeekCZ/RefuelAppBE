from services.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    display_name = db.Column(db.String(120))
    is_disabled = db.Column(db.Boolean, default=False)
    primary_car_id = db.Column(db.Integer, nullable=True)
    preferred_currency_id = db.Column(db.Integer, nullable=True)
    password = db.Column(db.String(255), nullable=False)  # <-- New field

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "displayName": self.display_name,
            "isDisabled": self.is_disabled,
            "primaryCarId": self.primary_car_id,
            "preferredCurrencyId": self.preferred_currency_id,
            # Don't include password in responses for security reasons
        }
