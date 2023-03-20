Feature: OrangeHrm Login
  Scenario: Login into OrangeHrm Homepage
    Given Launch the Chrome Browser
    When User enters the Orangehrm homepage
    And User enter the username
    And User enters the password
    #And User enter the username "Admin"
    #And User enters the password "admin123"
    Then Click on login button
    Then User enters in the orangehrm dashboard page