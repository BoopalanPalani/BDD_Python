Feature: OrangeHrm login

  Scenario: Login into OrangeHrm Homepage
    Given Launch the Chrome Browser
    When User enters the Orangehrm homepage
    And User enter the username and password
    Then Click on login button
    Then User enters in the orangehrm dashboard page

  Scenario: Search User
    Given Launch the Chrome Browser
    When User enters the Orangehrm homepage
    And User enter the username and password
    Then Click on login button
    When navigate to search page
    Then Search page should display

  Scenario: Advanced Search User
   Given Launch the Chrome Browser
    When User enters the Orangehrm homepage
    And User enter the username and password
    Then Click on login button
    When navigates to advanced search user page
    Then Advanced search page should display
