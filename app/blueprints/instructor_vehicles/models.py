from app.extensions import db


class InstructorVehicle(db.Model):
    __tablename__ = "instructor_vehicles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    instructor_id = db.Column(
        db.Integer, db.ForeignKey("instructors.id"), nullable=False
    )
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.id"), nullable=False)
