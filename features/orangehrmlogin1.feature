Feature: OrangeHrm Login
  Scenario Outline: Login into OrangeHrm Homepage
    Given Launch the Chrome Browser
    When User enters the Orangehrm homepage
    And User enter the "<username>"
    And User enters the "<password>"
    Then Click on login button
    Then User enters in the orangehrm dashboard page

    Examples:
    |username|Password|
    |admin   |admin123|
    |Admin   |admin123|
    |admin@  |admin@123|