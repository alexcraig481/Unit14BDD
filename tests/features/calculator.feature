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
  Scenario: Numerical year and month in respective acceptable range
    Given the user enters a year in acceptable range
    And the user enters a month in acceptable range
    When the user submits the data
    Then the retirement calculation will start

# Year out of range
  Scenario: Numerical year of birth outside of the acceptable range
    Given the user enters a year outside of the acceptable range
    When the user submits the data
    Then an exception will be raised

# Month out of range
  Scenario: Numerical birth month outside of the acceptable range
    Given the user enters a month outside of the acceptable range
    When the user submits the data
    Then an exception will be raised


# Rule: Year and Month of Birth entries must successfully convert to integers

# Year can convert
  Scenario: Year input can convert to an integer
    Given the user enters characters for the birth year that can be converted to an integer
    When the user submits the data
    Then the entry for year can proceed to be checked against the acceptable range

# Year can not convert
  Scenario: Year input cannot convert to an integer
    Given the user enters characters for the year that cannot be converted to an integer
    When the user submits the data
    Then an exception will be raised

# Month can convert
  Scenario: Month input can convert to an integer
    Given the user enters characters for the birth month that can be converted to an integer
    When the user submits the data
    Then the entry for month can proceed to be checked against the acceptable range

# Month can not convert
  Scenario: Month input cannot convert to an integer
    Given the user enters characters for the month that cannot be converted to an integer
    When the user submits the data
    Then an exception will be raised

# Rule: Accurate Social Security full benefit eligibility age and date will be displayed
  Scenario: Accurate age and date are displayed after input submitted
    Given the user has submitted an acceptable year of birth
    And the user has submitted an acceptable month of birth
    When the user submits the data
    Then the eligibility age and date will be displayed