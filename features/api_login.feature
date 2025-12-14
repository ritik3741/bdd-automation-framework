Feature: API User Validation

  @api @regression
  Scenario: Fetch user details
    Given user API endpoint is available
    When I send a GET request for user
    Then API should return valid user response
