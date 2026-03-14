from ..database import db
import uuid
from datetime import datetime

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String)
    email = db.Column(db.String)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    invoices = db.relationship("Invoice", backref="customer", lazy=True)