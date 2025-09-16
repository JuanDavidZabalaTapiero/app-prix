from sqlalchemy import func

from app.extensions import db


class LicenseCategory(db.Model):
    __tablename__ = "license_categories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(
        db.DateTime, server_default=func.current_timestamp(), nullable=False
    )

    # RELATIONSHIPS
    enrollments = db.relationship("Enrollment", back_populates="category")
