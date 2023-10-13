Feature: Verify Deals on New Arrivals Hover

  Scenario: User hovers over New Arrivals and verifies deals visibility
    Given Open Amazon product B074TBCSC8 page
    When User hovers over "New Arrivals"
    Then Verify user sees the deals

