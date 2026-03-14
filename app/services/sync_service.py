from ..models.customer import Customer
from ..models.invoice import Invoice
from ..models.payment import Payment
from ..database import db
from datetime import datetime

from ..integrations.accounting_client import (
    fetch_customers,
    fetch_invoices,
    fetch_payments
)


def sync_data():

    for c in fetch_customers():

        existing = db.session.get(Customer, c["id"])
        if not existing:
            customer = Customer(
                id=c["id"],
                name=c["name"],
                email=c["email"]
            )

            db.session.add(customer)

    for i in fetch_invoices():
        existing = db.session.get(Invoice, i["id"])
        if not existing:

            invoice = Invoice(
                id=i["id"],
                customer_id=i["customer_id"],
                amount=i["amount"],
                due_date=datetime.strptime(i["due_date"], "%Y-%m-%d").date()
            )

            db.session.add(invoice)

    for p in fetch_payments():
        
        existing = db.session.get(Payment, p["id"])

        if not existing:
            payment = Payment(
                id=p["id"],
                invoice_id=p["invoice_id"],
                amount=p["amount"],
                paid_at=datetime.strptime(p["paid_at"], "%Y-%m-%d").date()
            )

            db.session.add(payment)

    db.session.commit()