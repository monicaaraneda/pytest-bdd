import pytest
import requests


@pytest.fixture
def response(user_id, user_type, amount, target_alias='monica'):
    url = 'https://qa.api.redpay.junngla.com/payment-token/generate'
    headers = {'Content-Type': 'application/json', 'x-forwarded-for': '::1'}
    data = {
        "enroller_user_id": user_id,
        "user_type": user_type,
        "token_type": "T0",
        "data": {"amount": amount, "target_alias": target_alias}
    }
    cert_file = '../certs/certificate.crt'
    key_file = '../certs/private.key'
    certs = (cert_file, key_file)
    response = requests.post(url, json=data, headers=headers, cert=certs)
    return response


@pytest.fixture
def user(user_type):
    """Fixture to create a user type context."""
    return {'type': user_type}
