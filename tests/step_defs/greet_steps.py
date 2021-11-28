
import pytest
from ui import Calculator
from pytest_bdd import scenario, given, when, then


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


###############################################################


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


##############################################################################


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
    session.check_for_exit_request()


@given("the user enters a month in acceptable range")
def acceptable_month(session):
    session.month_prompt_response = 12
    session.check_for_exit_request()


@when("the user submits the data")
def submit_data(session):
    session.user_calculation.set_year(session.year_prompt_response)
    session.user_calculation.set_month(session.month_prompt_response)


@then("the retirement calculation will start")
def retirement_calc_runs(session):
    assert "Social Security Full Benefit \nYour Age and Date Eligibility" == \
           session.user_calculation.run_calculation()


