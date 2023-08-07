# Created by matthewandre at 2/20/23
Feature: Test Scenario to verify that amazon opens clicks on the cart icon and verifies that your amazon cart is empty


  Scenario: User opens amazon clicks on the cart icon
    Given Open Amazon page
    When User Click on the cart icon
    Then Verify your amazon cart is empty
