from app.extensions import db


class Instructor(db.Model):
    __tablename__ = "instructors"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    contract = db.Column(db.String(100), nullable=False)
