from app.extensions import db
from sqlalchemy import func

class LicenseCategory(db.Model):
    __tablename__ = "license_categories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.current_timestamp(), nullable=False)