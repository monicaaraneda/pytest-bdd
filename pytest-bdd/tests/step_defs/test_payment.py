import requests
from pytest_bdd import scenarios, given, when, then, parsers
import pytest
from src.payment.Payment import Payment

scenarios('../features/payment.feature')


@given(parsers.parse('I am a "{user_type}"'), target_fixture="user")
def user(user_type):
    return {'type': user_type}


@when(parsers.parse('I request a payment token for "{user_id}" with an amount of "{amount}"'),
      target_fixture="response")
def response(user, user_id, amount):
    print(f"User Type: {user['type']}, ID: {user_id}, Amount: {amount}")
    # Assuming a function `make_payment_request` that performs the API call
    return make_payment_request(user_id, user['type'], amount)


@then('I should get a successful response')
def verify_successful_response(response):
    assert response.status_code == 200, f"Expected 200, got {response.status_code}. Message: {response.text}"


def make_payment_request(user_id, user_type, amount):
    try:
        # Convert amount to integer
        amount = int(amount)
    except ValueError:
        # Handle the case where amount is not convertible to an integer
        return MockResponse(400, "Invalid amount - amount must be a numeric value")

    # Now, perform the check
    if amount <= 0:
        return MockResponse(400, "Invalid amount - amount must be positive")

    elif user_type not in ['collector', 'payer']:
        return MockResponse(403, "Unauthorized user type")  # Forbidden
    else:
        return MockResponse(200, f"Payment of {amount} processed for user {user_id}")  # Success


class MockResponse:
    # A simple class to mock responses from requests.post
    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text


@given(parsers.parse('I am a "{user_type}"'))
def set_user_type(user_type):
    # Assuming you have some context or model to set the user type,
    # For example, setting up a test user object:
    user = {'type': user_type}
    return user
