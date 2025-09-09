from app.extensions import db
from sqlalchemy import func

class InstructorVehicle(db.Model):
    __tablename__ = "instructor_vehicles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey("instructors.id"), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.id"), nullable=False)

class Enrollment(db.Model):
    __tablename__ = "enrollments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("license_categories.id"), nullable=False)
    is_completed = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.current_timestamp(), nullable=False)

class Lesson(db.Model):
    __tablename__ = "lessons"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    lesson_number = db.Column(db.Integer, nullable=False)
    enrollment_id = db.Column(db.Integer, db.ForeignKey("enrollments.id"), nullable=False)
    instructor_vehicle_id = db.Column(db.Integer, db.ForeignKey("instructor_vehicles.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    lesson_type = db.Column(db.String(20), nullable=False)
    is_paid = db.Column(db.Boolean, default=False, nullable=False)
    notes = db.Column(db.String(255))
