Feature: Login functionality

  @regression @login
  Scenario: Valid user login
    Given user is on login page
    When user enters valid username and password
    Then user should be logged in successfully
