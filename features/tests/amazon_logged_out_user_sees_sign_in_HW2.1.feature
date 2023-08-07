Feature: Test Scenario to verify that logged out user sees Sign In when clicking on Returns and Orders


  Scenario: A logged out user sees Sign In when clicking on Returns and Orders
    Given Open Amazon page
    When User Click on Returns and Orders icon
    Then Verify Sign in page opened

