from services.db import db

class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency_id = db.Column(db.Integer, unique=True, nullable=False)
    currency_code = db.Column(db.String(10), nullable=False)
    currency_name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "currencyId": self.currency_id,
            "currencyCode": self.currency_code,
            "currencyName": self.currency_name,
        }
