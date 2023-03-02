# Created by matthewandre at 2/24/23
Feature: Test Scenario to add a product you want into the cart and verify it's there


  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Input text Sandals
    When Click on search button
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has product