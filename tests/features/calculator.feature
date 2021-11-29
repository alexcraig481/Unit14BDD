# Created by AlexC at 11/27/2021
Feature:Retirement Calculation
  # ************************************Enter feature description here

# Rule: User can press Enter to exit the application

# Exit at Year
  Scenario: User exits at year of birth prompt
    Given the year prompt is displayed
    When enter is pressed
    Then the program ends

# Exit at Month
    Scenario: User exits at month of birth prompt
    Given the month prompt is displayed
    When enter is pressed
    Then the program ends


# Rule: Year and Month of Birth must be in respective acceptable range

# Both in range
  Scenario: User enters numerical year and month in respective acceptable range
    Given the user enters a year in acceptable range
    And the user enters a month in acceptable range
    When the user submits the data
    Then the retirement calculation will start

# Year out of range
  Scenario: User enters a year outside of the acceptable range
    Given the user enters a year outside of the acceptable range
    When the user submits the data
    Then an exception will be raised

# Month out of range
  Scenario: User enters a month outside of the acceptable range
    Given the user enters a month outside of the acceptable range
    When the user submits the data
    Then an exception will be raised


# Rule: Year and Month of Birth entries must successfully convert to integers

# Both convert
  Scenario: User enters characters for year and month that can be converted to integers
    Given the user enters characters for the birth year that can be converted to an integer
    And the user enters characters for the birth month that can be converted to an integer
    When the user submits the data
    Then the entries can proceed to be checked against their respective acceptable range