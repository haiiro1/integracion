# transbank_integration.py

import requests

def validate_payment(commerce_id, commerce_payment_id, service_id, amount, client_id):
    url = "https://api.transbank.cl/transbank/publico/patpass/payments"
    headers = {
        "Content-Type": "application/json",
        "X-Client-Id": client_id
    }
    payload = {
        "commerceId": commerce_id,
        "commercePaymentId": commerce_payment_id,
        "serviceId": service_id,
        "amount": amount
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def issue_payment(commerce_id, commerce_payment_id, processor_payment_id, service_id, client_id):
    url = "https://api.transbank.cl/transbank/publico/patpass/payments"
    headers = {
        "Content-Type": "application/json",
        "X-Client-Id": client_id
    }
    payload = {
        "commerceId": commerce_id,
        "commercePaymentId": commerce_payment_id,
        "processorPaymentId": processor_payment_id,
        "serviceId": service_id
    }
    response = requests.put(url, headers=headers, json=payload)
    return response.json()

def get_payment(commerce_id, commerce_payment_id, processor_payment_id, service_id, client_id):
    url = "https://api.transbank.cl/transbank/publico/patpass/payments"
    headers = {
        "Content-Type": "application/json",
        "X-Client-Id": client_id
    }
    params = {
        "commerceId": commerce_id,
        "commercePaymentId": commerce_payment_id,
        "processorPaymentId": processor_payment_id,
        "serviceId": service_id
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()
