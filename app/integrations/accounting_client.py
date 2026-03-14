import requests

BASE_URL = "http://localhost:5001"

def fetch_customers():
    return requests.get(f"{BASE_URL}/customers").json()

def fetch_invoices():
    return requests.get(f"{BASE_URL}/invoices").json()

def fetch_payments():
    return requests.get(f"{BASE_URL}/payments").json()