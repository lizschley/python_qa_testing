''' Any date or time convenience methods should go here '''
from datetime import datetime, timedelta, timezone
from dateutil.relativedelta import relativedelta
from dateutil import tz
import pytz
import utilities.utils as utils


def datetime_from_date_str(datetime_string, date_format):
    return datetime.strptime(datetime_string, date_format)


def timediff_from_datetime(oper='-', units=None, dt=None):
    '''
    timediff_from_datetime takes in variables and returns string of representation of the difference
    between now and the units operator and amount passed in

    :param oper: operator (minus or plus), defaults to '-'
    :type oper: str, optional
    :param units: Expects dictionary, for ex: {'weeks': 12}, defaults to None
    :type units: dictionary, optional
    :return: representation of date figured out to use in where statement
    :rtype: str
    '''
    use_date = ensuring_date_is_timezone_aware(dt)
    if utils.key_in_dictionary(units, 'years'):
        return timediff_in_years(use_date, units['years'])

    units = {'days': 1} if units is None else units
    if oper == '-':
        new_date = use_date - timedelta(**units)
    elif oper == '+':
        new_date = use_date + timedelta(**units)
    return new_date


def timediff_in_years(use_date, num):
    return use_date - relativedelta(years=num)




def ensuring_date_is_timezone_aware(dt=None):
    # Always changes to UTC
    if not dt:
        return datetime.now(timezone.utc)
    elif not dt.tzinfo:
        return dt.replace(tzinfo=pytz.utc)
    return dt


def string_from_datetime_default_now(dt):
    if not dt:
        dt = datetime.now()
    return dt.strftime('%Y%m%d_%H%M%S')


def formatted_datetime_utc_from_datetime(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%S.000Z[UTC]')


def number_days_before_or_after_given_datetime_returns_string_date(**kwargs):
    op = kwargs.get('op', '')
    num_days = kwargs.get('num_days', 2)
    date = kwargs.get('date', datetime.now(tz=tz.tzlocal()))
    new_date = date
    if op == 'minus':
        new_date = date - timedelta(days=num_days)
    elif op == 'plus':
        new_date = date + timedelta(days=num_days)
    return new_date.strftime('%Y-%m-%d')


def current_date_string():
    now = datetime.now(tz=tz.tzlocal())
    return now.strftime('%Y-%m-%d')


# Note: this assumes that format is YYYY MM DD with delimiters
def datetime_from_date_only_string(date_only_string, delimiter='-'):
    date_parts = date_only_string.split(delimiter)
    year = int(date_parts[0])
    month = int(date_parts[1])
    day = int(date_parts[2])
    return datetime(year, month, day, 0, 0, 0, 000000, tzinfo=timezone.utc)


def postgres_friendly_datetime(use_datetime=None):
    '''
    postgres_friendly_datetime takes a datetime object and writes it to a string
    in a format that can be used to update postgres
    :param datetime_obj: passed in datetime obj
    :type datetime_obj: datetime.datetime
    :return: string representaion of the object that postgres understands
    :rtype: str
    '''
    if use_datetime is None:
        use_datetime = datetime.now(tz.UTC)
    str_dt = datetime.isoformat(use_datetime)
    temp = str_dt.split('.')
    return temp[0] + '.' + temp[1][0:3] + '+0000'


def get_current_epoch_date(dt=None):
    '''
    get_current_epoch_date returns current date in seconds from 1/1/1970 to use for versioning on S3

    :return: epoch date in seconds
    :rtype: int
    '''
    if dt is None:
        dt = datetime.now()
    epoch = int(dt.timestamp())
    return epoch


def seconds_between_two_dates(**kwargs):
    earlier = kwargs.get('earlier', datetime.now())
    later = kwargs.get('later', datetime.now())
    difference = (later - earlier)
    return round(difference.total_seconds())
