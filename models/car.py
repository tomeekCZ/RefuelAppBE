from services.db import db

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    vin = db.Column(db.String(100))
    color = db.Column(db.String(50))
    fuel_type = db.Column(db.String(50))
    description = db.Column(db.Text)
    is_archived = db.Column(db.Boolean, default=False)
    licence_plate = db.Column(db.String(100), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "brand": self.brand,
            "model": self.model,
            "vin": self.vin,
            "color": self.color,
            "fuelType": self.fuel_type,
            "description": self.description,
            "isArchived": self.is_archived,
            "licencePlate": self.licence_plate,
        }
