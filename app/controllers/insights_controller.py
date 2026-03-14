from flask import Blueprint, jsonify, request
from ..services.sync_service import sync_data
from ..services.insight_service import customer_balance, overdue_invoices



insights_bp = Blueprint("insights", __name__)

@insights_bp.route("/sync")
def sync():
    sync_data()
    return jsonify({"message": "Data synced"})


@insights_bp.route("/customers/<customer_id>/balance")
def get_customer_balance(customer_id):  

    result = customer_balance(customer_id)

    return jsonify(result)

@insights_bp.route("/invoices/overdue")
def get_overdue():

    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 20, type=int)

    data = overdue_invoices(page, limit)

    return jsonify(data)