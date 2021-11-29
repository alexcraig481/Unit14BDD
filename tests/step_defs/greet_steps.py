
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
@scenario("../features/calculator.feature", "User enters numerical year and month in respective acceptable range")
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
@scenario("../features/calculator.feature", "User enters a year outside of the acceptable range")
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
@scenario("../features/calculator.feature", "User enters a month outside of the acceptable range")
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

# Rule Year and Month of Birth entries must successfully convert to integers

# Both convert
@scenario("../features/calculator.feature", "User enters characters for year and month"
                                            " that can be converted to integers")
def test_user_input_conversion():
    pass


# Fixture
@pytest.fixture
def session():
    return Calculator()


@given("the user enters characters for the birth year that can be converted to an integer")
def convertable_year(session):
    session.year_prompt_response = "4444"


@given("the user enters characters for the birth month that can be converted to an integer")
def convertable_month(session):
    session.month_prompt_response = "88"


@when("the user submits the data", target_fixture="submit_data")
def submit_data(session):
    try:
        session.user_calculation.set_year(session.year_prompt_response)
    except ValueError as err:
        year_err = str(err)
    try:
        session.user_calculation.set_month(session.month_prompt_response)
    except ValueError as err:
        month_err = str(err)
    return month_err, year_err


@then("the entries can proceed to be checked against their respective acceptable range")
def proceed_to_range_check(submit_data):
    month_err, year_err = submit_data
    assert month_err == "Month entered outside acceptable range"
    assert year_err == "Year entered outside acceptable range"
