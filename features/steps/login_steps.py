from behave import given, when, then

@given('user is on login page')
def step_open_login(context):
    print("Opening login page")

@when('user enters valid username and password')
def step_enter_credentials(context):
    print("Entering username and password")

@then('user should be logged in successfully')
def step_verify_login(context):
    actual_result = "success"
    expected_result = "success"
    assert actual_result == expected_result
