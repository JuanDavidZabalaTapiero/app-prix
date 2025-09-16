from sqlalchemy import func

from app.extensions import db


class Enrollment(db.Model):
    __tablename__ = "enrollments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    category_id = db.Column(
        db.Integer, db.ForeignKey("license_categories.id"), nullable=False
    )
    is_completed = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(
        db.DateTime, server_default=func.current_timestamp(), nullable=False
    )

    # RELATIONSHIPS
    student = db.relationship("Student", back_populates="enrollments")
    category = db.relationship("LicenseCategory", back_populates="enrollments")
