

import sys
from retire import RetireCalculation


class Calculator:
    def __init__(self):
        """Initialize Calculator"""
        self.year_prompt_response = 0
        self.month_prompt_response = 0
        self.user_calculation = RetireCalculation()

    def run_calculator(self):
        """Main Program"""
        while True:
            self.get_birth_year()
            self.check_for_exit_request()
            self.user_calculation.set_year(self.year_prompt_response)
            self.get_birth_month()
            self.check_for_exit_request()
            self.user_calculation.set_month(self.month_prompt_response)
            print(self.user_calculation.run_calculation())

    def get_birth_year(self):
        year = input("Enter your year of birth or press Enter to exit: ")
        self.year_prompt_response = year

    def get_birth_month(self):
        month = input("Enter the month of your birth: ")
        self.month_prompt_response = month

    def check_for_exit_request(self):
        if self.year_prompt_response == "" or self.month_prompt_response == "":
            sys.exit()


if __name__ == "__main__":
    # Make Calculator instance and run program
    session = Calculator()
    session.run_calculator()
