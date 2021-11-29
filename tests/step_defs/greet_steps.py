
import pytest
from ui import Calculator
from pytest_bdd import scenario, given, when, then


# Rule: User can press Enter to exit the application

# Exit at Year
@scenario("../features/calculator.feature", "User exits at year of birth prompt")
def test_year_exit():
    pass


@given("the year prompt is displayed", target_fixture="session")
def session():
    return Calculator()


@when("enter is pressed")
def mock_year_prompt(session):
    session.year_prompt_response = ""


@then("the program ends")
def program_ends(session):
    with pytest.raises(SystemExit):
        session.check_for_exit_request()


#######################################################################################

# Exit at Month
@scenario("../features/calculator.feature", "User exits at month of birth prompt")
def test_month_exit():
    pass


@given("the month prompt is displayed", target_fixture="session")
def session():
    return Calculator()


@when("enter is pressed")
def mock_month_prompt(session):
    session.month_prompt_response = ""


@then("the program ends")
def program_ends(session):
    with pytest.raises(SystemExit):
        session.check_for_exit_request()


#######################################################################################

# Rule: Year and Month of Birth must be in respective acceptable range

# Both acceptable
@scenario("../features/calculator.feature", "Numerical year and month in respective acceptable range")
def test_acceptable_range():
    pass


# Fixture
@pytest.fixture
def session():
    return Calculator()


@given("the user enters a year in acceptable range")
def acceptable_year(session):
    session.year_prompt_response = 1954


@given("the user enters a month in acceptable range")
def acceptable_month(session):
    session.month_prompt_response = 12


@when("the user submits the data")
def submit_data(session):
    session.user_calculation.set_year(session.year_prompt_response)
    session.user_calculation.set_month(session.month_prompt_response)


@then("the retirement calculation will start")
def retirement_calc_runs(session):
    assert "Social Security Full Benefit \nYour Age and Date Eligibility" == \
           session.user_calculation.run_calculation()

#######################################################################################


# Year not acceptable
@scenario("../features/calculator.feature", "Numerical year of birth outside of the acceptable range")
def test_out_of_range_year():
    pass


# Fixture
@pytest.fixture
def session():
    return Calculator()


@given("the user enters a year outside of the acceptable range")
def out_of_range_year(session):
    session.year_prompt_response = 1899


@when("the user submits the data", target_fixture="submit_data")
def submit_data(session):
    try:
        session.user_calculation.set_year(session.year_prompt_response)
    except ValueError as err:
        assert str(err) == "Year entered outside acceptable range"


@then("an exception will be raised")
def exception_raised(submit_data):
    pass


#######################################################################################

# Month not acceptable
@scenario("../features/calculator.feature", "Numerical birth month outside of the acceptable range")
def test_out_of_range_month():
    pass


# Fixture
@pytest.fixture
def session():
    return Calculator()


@given("the user enters a month outside of the acceptable range")
def out_of_range_month(session):
    session.month_prompt_response = 13


@when("the user submits the data", target_fixture="submit_data")
def submit_data(session):

    try:
        session.user_calculation.set_month(session.month_prompt_response)
    except ValueError as err:
        return str(err)


@then("an exception will be raised")
def exception_raised(submit_data):
    assert submit_data == "Month entered outside acceptable range"


###############################################################

# Rule: User input for year and month of birth must successfully convert to integers

# Year can be converted
@scenario("../features/calculator.feature", "Year input can convert to an integer")
def test_year_convert():
    pass


# Fixture
@pytest.fixture
def session():
    return Calculator()


@given("the user enters characters for the birth year that can be converted to an integer")
def valid_year(session):
    session.year_prompt_response = "4444"


@when("the user submits the data", target_fixture="submit_data")
def submit_data(session):
    try:
        session.user_calculation.set_year(session.year_prompt_response)
    except ValueError as err:
        return str(err)

    
@then("the entry for year can proceed to be checked against the acceptable range")
def range_check(submit_data):
    assert submit_data == "Year entered outside acceptable range"


################################################################

# Year can NOT be converted

@scenario("../features/calculator.feature", "Year input cannot convert to an integer")
def test_year_convert_fail():
    pass


# Fixture
@pytest.fixture
def session():
    return Calculator()


@given("the user enters characters for the year that cannot be converted to an integer")
def invalid_year(session):
    session.year_prompt_response = "4OO"


@when("the user submits the data", target_fixture="submit_data")
def submit_data(session):
    try:
        session.user_calculation.set_year(session.year_prompt_response)
    except ValueError as err:
        return str(err)


@then("an exception will be raised")
def range_check(submit_data):
    assert "invalid literal for int() " in submit_data


##################################################################

# Month can be converted
@scenario("../features/calculator.feature", "Month input can convert to an integer")
def test_month_convert():
    pass


# Fixture
@pytest.fixture
def session():
    return Calculator()


@given("the user enters characters for the birth month that can be converted to an integer")
def valid_month(session):
    session.month_prompt_response = "13"


@when("the user submits the data", target_fixture="submit_data")
def submit_data(session):
    try:
        session.user_calculation.set_month(session.month_prompt_response)
    except ValueError as err:
        return str(err)


@then("the entry for month can proceed to be checked against the acceptable range")
def range_check(submit_data):
    assert submit_data == "Month entered outside acceptable range"


###############################################################

# Month can NOT be converted
@scenario("../features/calculator.feature", "Month input cannot convert to an integer")
def test_month_convert_fail():
    pass


# Fixture
@pytest.fixture
def session():
    return Calculator()


@given("the user enters characters for the month that cannot be converted to an integer")
def invalid_month(session):
    session.month_prompt_response = "l0"


@when("the user submits the data", target_fixture="submit_data")
def submit_data(session):
    try:
        session.user_calculation.set_month(session.month_prompt_response)
    except ValueError as err:
        return str(err)
                                                                                     

@then("an exception will be raised")
def range_check(submit_data):
    assert "invalid literal for int() " in submit_data

###############################################################

# Rule: Accurate Social Security full benefit eligibility age and date will be displayed


@scenario("../features/calculator.feature", "Accurate age and date are displayed after input submitted")
def test_accurate_results():
    pass


# Fixture
@pytest.fixture
def session():
    return Calculator()


@given("the user has submitted an acceptable year of birth")
def acceptable_year(session):
    session.year_prompt_response = "1954"


@given("the user has submitted an acceptable month of birth")
def acceptable_month(session):
    session.month_prompt_response = "8"


@when("the user submits the data")
def data_submit(session):
    session.user_calculation.set_year(session.year_prompt_response)
    session.user_calculation.set_month(session.month_prompt_response)

    
@then("the eligibility age and date will be displayed")
def check_results():
    pass