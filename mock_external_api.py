from flask import Flask, jsonify

app = Flask(__name__)

# Mock data simulating an external accounting system

customers = [
    {"id": "1", "name": "Acme Corp", "email": "finance@acme.com"},
    {"id": "2", "name": "Beta Industries", "email": "accounts@beta.com"}
]

invoices = [
    {"id": "101", "customer_id": "1", "amount": 10000, "due_date": "2026-03-01"},
    {"id": "102", "customer_id": "1", "amount": 5000, "due_date": "2026-03-02"},
    {"id": "103", "customer_id": "2", "amount": 7000, "due_date": "2026-03-05"}
]

payments = [
    {"id": "501", "invoice_id": "101", "amount": 4000, "paid_at": "2026-03-02"},
    {"id": "502", "invoice_id": "103", "amount": 7000, "paid_at": "2026-03-06"}
]


@app.route("/customers", methods=["GET"])
def get_customers():
    return jsonify(customers)


@app.route("/invoices", methods=["GET"])
def get_invoices():
    return jsonify(invoices)


@app.route("/payments", methods=["GET"])
def get_payments():
    return jsonify(payments)


if __name__ == "__main__":
    print("Mock Accounting API running on http://127.0.0.1:5001")
    app.run(host="127.0.0.1", port=5001, debug=True)