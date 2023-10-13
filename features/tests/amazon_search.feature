Feature: Search for a Laptops in the Computer Department

  Scenario: User can use dropdown and search for a Laptop in the Computer Department

    Given Open Amazon page
    When Click department dropdown
    And Click on Computers department
    And Input Laptops into search field
    And Click on search icon
    Then Product results for "Laptops" are shown
