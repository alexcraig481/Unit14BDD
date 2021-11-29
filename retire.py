

class RetireCalculation:
    def __init__(self):
        self._year = 0
        self._month = 0

    def set_year(self, year):
        year = int(year)
        if 1900 <= year <= 2021:
            self._year = year
            print("year set", self._year)
        else:
            raise ValueError("Year entered outside acceptable range")

    def set_month(self, month):
        month = int(month)
        if 1 <= month <= 12:
            self._month = month
            print("month set", self._month)
        else:
            raise ValueError("Month entered outside acceptable range")

    def run_calculation(self):
        self
        return "Social Security Full Benefit \nYour Age and Date Eligibility"
