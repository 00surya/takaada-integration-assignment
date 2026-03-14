from ..models.customer import Customer
from ..models.invoice import Invoice
from ..models.payment import Payment
from datetime import datetime

def customer_balance(customer_id):

    customer = Customer.query.get(customer_id)

    if not customer:
        return {"error": "Customer not found"}

    invoices = Invoice.query.filter_by(customer_id=customer_id).all()

    total_invoiced = sum(i.amount for i in invoices)

    invoice_ids = [i.id for i in invoices]

    payments = Payment.query.filter(
        Payment.invoice_id.in_(invoice_ids)
    ).all()

    total_paid = sum(p.amount for p in payments)

    outstanding = total_invoiced - total_paid

    return {
        "customer_id": customer_id,
        "total_invoiced": total_invoiced,
        "total_paid": total_paid,
        "outstanding_balance": outstanding
    }



def overdue_invoices(page=1, limit=20):

    today = datetime.today().date()

    invoices = (
        Invoice.query
        .filter(Invoice.due_date < today)
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )

    invoice_ids = [i.id for i in invoices]

    payments = Payment.query.filter(
        Payment.invoice_id.in_(invoice_ids)
    ).all()

    payment_map = {}

    for p in payments:
        payment_map.setdefault(p.invoice_id, 0)
        payment_map[p.invoice_id] += p.amount

    result = []

    for invoice in invoices:

        paid = payment_map.get(invoice.id, 0)

        if paid < invoice.amount:

            result.append({
                "invoice_id": invoice.id,
                "customer_id": invoice.customer_id,
                "amount_due": invoice.amount - paid,
                "due_date": invoice.due_date
            })

    return result