from ..database import db
import uuid
from datetime import datetime

class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    invoice_id = db.Column(
        db.String(36),
        db.ForeignKey("invoices.id")
    )

    amount = db.Column(db.Float)
    paid_at = db.Column(db.Date)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)