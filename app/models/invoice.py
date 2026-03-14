from ..database import db
import uuid
from datetime import datetime


class Invoice(db.Model):
    __tablename__ = "invoices"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    customer_id = db.Column(
        db.String(36),
        db.ForeignKey("customers.id")
    )

    amount = db.Column(db.Float)
    due_date = db.Column(db.Date)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    payments = db.relationship("Payment", backref="invoice", lazy=True)