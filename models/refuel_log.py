from services.db import db

class RefuelLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    car_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(10), nullable=False)  # ISO format: YYYY-MM-DD
    mileage = db.Column(db.Float, nullable=False)
    liters = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    currency_id = db.Column(db.Integer, nullable=False)
    station_brand = db.Column(db.String(100))
    comments = db.Column(db.Text)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "carId": self.car_id,
            "date": self.date,
            "mileage": self.mileage,
            "liters": self.liters,
            "price": self.price,
            "currencyId": self.currency_id,
            "stationBrand": self.station_brand,
            "comments": self.comments,
            "lat": self.lat,
            "lon": self.lon,
        }
