
import csv
import datetime
import random
import string


def string_from_list_that_contains_substring(string_list, search_for):
    # search list for string containing substring
    # this is not currently being used in this code base
    for str in string_list:
        if search_for in str:
            return str
    return ''


def loop_x_times_to_run_method(method, num_times):
    for x in range(num_times):
        var = method()
        print(var)


def search_string_for_substring_from_list(substring_list, string):
    ''' search for string containing substring in list
        EXAMPLE of usage:
        1. substring_list is search_for from ui_tests.toml
        2. The string is the feature name, so basically we are looking for a substring in a string
        3. If the feature name (string) contains the substring, return the substring
        4. The substring is a key for the user_type lookup table in data/environment.py
           It will give you the information needed to look up the user to log in with
    '''
    for search_for in substring_list:
        if search_for in string:
            return search_for
    return ''


def error_dict_from_list(seperator, errors, begin_string):
    if len(errors) == 0:
        return {}
    error_str = begin_string + seperator.join(errors)
    return {'error': error_str}


def item_in_list(in_item, item_list):
    for item in item_list:
        if in_item == item:
            return True
    return False


def key_not_in_dictionary(dict_to_check, key):
    '''
    key_not_in_dictionary returns true if key not in dictionary, else false
    :param dict_to_check: pass in the dictionary in question
    :type dict_to_check: dictionary
    :param key: key we are looking for
    :type key: depends on input
    :return: True if key is in dict_to_check else false
    :rtype: bool
    '''
    default = 'hopefully$$** never___ TO return~~~%^&'
    val = dict_to_check.get(key, default)
    return val == default


def key_in_dictionary(dict_to_check, key):
    '''
    key_in_dictionary returns true if key in dictionary, else false
    :param dict_to_check: pass in the dictionary in question
    :type dict_to_check: dictionary
    :param key: key we are looking for
    :type key: string
    :return: False if key not in dict_to_check else True
    :rtype: bool
    '''
    default = 'hopefully$$** never___ TO return~~~%^&'
    val = dict_to_check.get(key, default)
    return val != default


def find_dict_from_list_by_key_and_value(dictionary_list, key, value):
    '''
    find_dict_from_list_by_value returns the correct dictionary, when you know the key and the value

    :param dictionary_list: list of dictionaries
    :param key: string
    :param value: string
    :rtype: dictionary
    '''
    for dict in dictionary_list:
        if key_in_dictionary(dict, key) and dict[key] == value:
            return dict
    return {}


def subset_list_by_key_and_value(dictionary_list, key, value):
    '''
    starting with a list of dictionaries, return a new list of only dictionaries that contain a given value within
    a given field

    :param dictionary_list: list of dictionaries
    :param key: string
    :param value: string
    :rtype: list
    '''
    new_list = []
    for dict in dictionary_list:
        if key_in_dictionary(dict, key) and value in dict[key]:
            new_list.append(dict)
    return new_list


def subset_list_by_key_and_real_value(dictionary_list, key):
    '''
    starting with a list of dictionaries, return a new list of only dictionaries that contain a given value within
    a given field

    :param dictionary_list: list of dictionaries
    :param key: string
    :param value: string
    :rtype: list
    '''
    new_list = []
    for dict in dictionary_list:
        if key_not_in_dictionary(dict, key):
            continue
        if dict[key]:
            new_list.append(dict)
    return new_list


# Note: default is 12 characters, random alpha numeric, mixed cases
# to get default send {} (empty dictionary)
def random_alpha_numeric(**kwargs):
    characters = retrieve_characters(**kwargs)
    # passing in {'min_length': 6, 'max_length': 8} would give you random alphanumeric string with length between 6 & 8
    min_length = kwargs.get('min_length', 12)
    max_length = kwargs.get('max_length', 12)
    rand_str = ''.join(random.choice(characters) for x in range(random.randint(min_length, max_length)))
    # print(rand_str)
    return rand_str


def retrieve_characters(**kwargs):
    alphanumeric = kwargs.get('alphanumeric', True)
    upper = kwargs.get('upper', True)
    lower = kwargs.get('lower', True)
    if alphanumeric:
        return alpha_numeric_characters(lower, upper)
    return alpha_characters(lower, upper)


def alpha_numeric_characters(lower=True, upper=True):
    return alpha_characters(lower, upper) + string.digits


def alpha_characters(lower=True, upper=True):
    if lower and upper:
        return string.ascii_letters
    if lower:
        return string.ascii_lowercase
    if upper:
        return string.ascii_uppercase


def random_num_start_end(start=1000000000, end=9999999999, prefix=1234567):
    random_num = random.randint(start, end)
    return f'{prefix}{random_num}'


def curr_datetime():
    now = datetime.datetime.now()
    return now.strftime('%m/%d/%Y %H:%M:%S')


def subtract_one_list_from_another(minuend, subtrahend):
    difference = [x for x in minuend if x not in subtrahend]
    return difference


def sort_list_of_dictionaries_by_key(dict_list_to_sort, key, reverse=False):
    if len(dict_list_to_sort) <= 0:
        return []
    if key_not_in_dictionary(dict_list_to_sort[0], key):
        return []
    if not reverse:
        return sorted(dict_list_to_sort, key=lambda x: x[key])
    else:
        return sorted(dict_list_to_sort, key=lambda x: x[key], reverse=True)


def string_from_integer_or_zero(num):
    original = num
    try:
        res = int(num)
    except ValueError as e:
        res = ''
    if res and res > 0:
        return original
    return None


def dict_from_csv_file(filepath):
    list_from_file = []
    with open(filepath) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list_from_file.append(row)
    return list_from_file


def random_item_in_array(items):
    idx = random.randint(0, len(items) - 1)
    return items[idx]
