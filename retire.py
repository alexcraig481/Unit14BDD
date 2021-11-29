

class RetireCalculation:
    def __init__(self):
        self._year = 0
        self._month = 0
        self._age_of_eligibility = {"years": 0, "months": 0}

    def set_year(self, year):
        year = int(year)
        if 1900 <= year <= 2021:
            self._year = year
        else:
            raise ValueError("Year entered outside acceptable range")

    def set_month(self, month):
        month = int(month)
        if 1 <= month <= 12:
            self._month = month
        else:
            raise ValueError("Month entered outside acceptable range")

    def run_calculation(self):
        retirement_year, retirement_month, age_years, age_month = self.calculate_retirement()
        return f"Social Security Full Benefit \nYour Age and Date Eligibility \n Age: {age_years} {age_month} months " \
               f"\nDate: {retirement_month}/1/{retirement_year}\n\n"

    def calculate_retirement(self):
        age_years, age_month = self._calculate_retirement_age()
        months_until_retirement_age = (age_years * 12) + age_month + self._month
        retirement_year = self._year + (months_until_retirement_age // 12)
        retirement_month = months_until_retirement_age % 12
        if retirement_month == 0:
            retirement_month = self._month
        return retirement_year, retirement_month, age_years, age_month

    def _calculate_retirement_age(self):
        if self._year <= 1937:
            return 65, 0
        elif self._year == 1938:
            return 65, 2
        elif self._year == 1939:
            return 65, 4
        elif self._year == 1940:
            return 65, 6
        elif self._year == 1941:
            return 65, 8
        elif self._year == 1942:
            return 65, 10
        elif 1943 <= self._year <= 1954:
            return 66, 0
        elif self._year == 1955:
            return 66, 2
        elif self._year == 1956:
            return 66, 4
        elif self._year == 1957:
            return 66, 6
        elif self._year == 1958:
            return 66, 8
        elif self._year == 1959:
            return 66, 10
        else:
            return 67, 0


