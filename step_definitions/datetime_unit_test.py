from behave import step
from datetime import datetime
import utilities.date_time as dt

SECONDS_IN_WEEK = 604800
# number_diff is passed into one test, but assumed in another (using passed in data, so asserting later)
NUMBER_DIFF = 3


# Ref: Scenario Outline --> you can get future or past dates in string format with YYYY-MM-DD
@step('using {original_date} and parameters that indicate {num_days} {unit} will return date in a YYYY-MM-DD format')
def future_or_past_date_only_string_datetime(context, original_date, num_days, unit):
    input_date = date_from_formatted_datetime_string(original_date, format_used='%Y-%m-%d')
    op = 'minus' if 'ago' in unit else 'plus'
    params = {
        'date': input_date,
        'op': op,
        'num_days': int(num_days)
    }
    returned_date = dt.number_days_before_or_after_given_datetime_returns_string_date(**params)
    context.scenario_level['returned_date'] = returned_date


@step('the date returned will be {expected_date}')
def proof_that_date_only_string_shows_two_days_in_past(context, expected_date):
    assert expected_date == context.scenario_level['returned_date']


# Ref: Scenario Outline --> examples of the timediff_from_datetime include years, weeks minutes, past & future datetime
@step('{original_date} will be formatted into a datetime record')
def create_datetime_record_with_given_format(context, original_date):
    context.feature_level['format_used'] = '%m-%d-%Y %H:%M:%S'
    context.scenario_level['original_datetime'] = datetime.strptime(original_date, context.feature_level['format_used'])
    assert isinstance(context.scenario_level['original_datetime'], datetime)


@step('with date arithmetic figuring {num} {unit} {direction} the expected date will be {expected_date}')
def do_arithetic_and_return_string_with_same_format(context, num, unit, direction, expected_date):
    expected_dt = datetime.strptime(expected_date, context.feature_level['format_used'])
    orig_dt = context.scenario_level['original_datetime']
    in_units = {unit: int(num)}
    if unit == 'weeks':
        context.feature_level['later'] = orig_dt
        context.feature_level['earlier'] = expected_dt
        assert in_units['weeks'] == NUMBER_DIFF
    oper = '-' if direction == 'ago' else '+'
    actual_dt = dt.timediff_from_datetime(oper, in_units, orig_dt)
    assert isinstance(actual_dt, datetime)
    assert actual_dt.year == expected_dt.year
    assert actual_dt.month == expected_dt.month
    assert actual_dt.day == expected_dt.day
    assert actual_dt.hour == expected_dt.hour
    assert actual_dt.minute == expected_dt.minute
    assert actual_dt.second == expected_dt.second


@step('the return will be three weeks from now')
def timediff_result_two_weeks_from_now(context):
    input = {
        'earlier': context.feature_level['input_datetime'],
        'later': context.feature_level['return_datetime']
    }
    assert dt.seconds_between_two_dates(**input) == NUMBER_DIFF * SECONDS_IN_WEEK


# Ref: Scenario --> you can get date diff by subtracting epoch dates (number of seconds from 1/1/1970)
@step('the epoch ints from two dates that are three weeks apart')
def two_epoch_dates_three_weeks_apart(context):
    later = context.feature_level.get('later', earlier_and_later_from_today_datetime()['later'])
    earlier = context.feature_level.get('earlier', earlier_and_later_from_today_datetime()['earlier'])
    context.scenario_level['earlier_int'] = dt.get_current_epoch_date(earlier)
    context.scenario_level['later_int'] = dt.get_current_epoch_date(later)


@step('the difference between them will be 3 times the number of seconds in a week')
def datetime_difference_in_seconds_is_three_weeks(context):
    earlier = context.scenario_level['earlier_int']
    later = context.scenario_level['later_int']
    assert later - earlier == NUMBER_DIFF * SECONDS_IN_WEEK


def date_from_formatted_datetime_string(start_date, format_used='%Y-%m-%d'):
    return datetime.strptime(start_date, format_used)


def earlier_and_later_from_today_datetime():
    oper = '+'
    units = {'weeks': NUMBER_DIFF}
    input_dt = dt.ensuring_date_is_timezone_aware()
    return {
        'earlier': input_dt,
        'later': dt.timediff_from_datetime(oper, units, input_dt)
    }
