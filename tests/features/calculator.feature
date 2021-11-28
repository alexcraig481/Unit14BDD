# Created by AlexC at 11/27/2021
Feature:Retirement Calculation
  # Enter feature description here

# Rule: User can press Enter to exit the application
  Scenario: User exits at year of birth prompt
    Given the year prompt is displayed
    When enter is pressed
    Then the program ends

    Scenario: User exits at month of birth prompt
    Given the month prompt is displayed
    When enter is pressed
    Then the program ends

# Rule: Year and Month of Birth must be in respective acceptable range
  Scenario: User enters numerical year and month in respective acceptable range
    Given the user enters a year in acceptable range
    And the user enters a month in acceptable range
    When the user submits the data
    Then the retirement calculation will start
