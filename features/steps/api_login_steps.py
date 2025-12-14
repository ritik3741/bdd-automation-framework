import requests
from behave import given, when, then

@given('user API endpoint is available')
def step_api_endpoint(context):
    context.url = "https://jsonplaceholder.typicode.com/users/1"

@when('I send a GET request for user')
def step_send_request(context):
    context.response = requests.get(context.url)

@then('API should return valid user response')
def step_validate_response(context):
    print("Status Code:", context.response.status_code)
    print("Response Body:", context.response.json())

    assert context.response.status_code == 200
    assert context.response.json()["id"] == 1
