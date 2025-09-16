from app.extensions import db


class Lesson(db.Model):
    __tablename__ = "lessons"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    lesson_number = db.Column(db.Integer, nullable=False)
    enrollment_id = db.Column(
        db.Integer, db.ForeignKey("enrollments.id"), nullable=False
    )
    instructor_vehicle_id = db.Column(
        db.Integer, db.ForeignKey("instructor_vehicles.id"), nullable=False
    )
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    lesson_type = db.Column(db.String(20), nullable=False)
    is_paid = db.Column(db.Boolean, default=False, nullable=False)
    notes = db.Column(db.String(255))
