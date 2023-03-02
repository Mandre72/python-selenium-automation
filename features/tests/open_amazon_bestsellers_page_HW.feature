# Created by matthewandre at 2/24/23
Feature: Test Scenario to open amazon Best Sellers page and verify there are 5 links

  Scenario:  Verify header has 5 links
    Given Open Amazon page
    When Click on Best Sellers
    Then Verify that header has 5 links
