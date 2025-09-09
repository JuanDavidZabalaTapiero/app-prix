from app.extensions import db

class Vehicle(db.Model):
    __tablename__ = "vehicles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    license_plate = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(20), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)