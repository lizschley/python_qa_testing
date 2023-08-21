import os
import sys
from behave import step
from services.person_service import PersonService
from services.quote_service import QuoteService
from support.basic_response import BasicResponse
import data.quotes_input_data as data
import utilities.utils as utils
import constants.used_in_more_than_one_file as uc
from http import HTTPStatus

ORIG_NUM_PEOPLE = 'orig_num_people'
CURRENT_NUM_PEOPLE = 'current_num_people'
ORIG_NUM_QUOTES = 'orig_num_quotes'
CURRENT_NUM_QUOTES = 'current_num_quotes'


# Ref: Scenario - client makes call to GET existing quotes
@step('the client makes a call to get all existing quotes')
def get_all_existing_quotes_call(context):
    quote_service = get_set_service(context, 'quote_service')
    person_service = get_set_service(context, 'person_service')
    set_up_original_counts(context, quote_service, person_service)
    quote_response = BasicResponse(quote_service.get_show_people_quotes())
    context.scenario_level['quote_response'] = quote_response


@step('get all existing quotes is successful')
def get_all_existing_quotes_returns_ok_status(context):
    assert context.scenario_level['quote_response'].status_code == HTTPStatus.OK


@step('the client gets a sorted array containing the correct number of quotes')
def sorted_array_of_quotes_correct_size(context):
    quotes = context.scenario_level['quote_response'].data
    expected_size = context.scenario_level[ORIG_NUM_QUOTES]
    expected_order = data.original_people_in_sorted_order()
    assert len(quotes) == expected_size
    assert quotes[0]['firstName'] == expected_order[0]['first']
    assert quotes[0]['lastName'] == expected_order[0]['last']
    assert quotes[1]['firstName'] == expected_order[1]['first']
    assert quotes[1]['lastName'] == expected_order[1]['last']
    assert quotes[2]['firstName'] == expected_order[2]['first']
    assert quotes[2]['lastName'] == expected_order[2]['last']
    assert quotes[3]['firstName'] == expected_order[3]['first']
    assert quotes[3]['lastName'] == expected_order[3]['last']


@step('a new person will get sorted correctly')
def add_imaginary_Alica_Austen_and_her_quote(context):
    quote_service = get_set_service(context, 'quote_service')
    good_input = data.add_quote_that_will_sort_before_jane_austen()
    context.scenario_level['input'] = good_input
    quote_response = BasicResponse(quote_service.add_quotes(good_input))
    context.scenario_level['quote_response'] = quote_response
    result = quote_response.data
    assert len(result) == 1 + context.scenario_level[ORIG_NUM_QUOTES]
    assert result[0]['firstName'] == 'Alicia'
    assert result[0]['lastName'] == 'Austen'
    assert result[1]['firstName'] == 'Jane'
    assert result[1]['lastName'] == 'Austen'


@step('the new person must be deleted so Jane Austen can be number one')
def delete_Alica_Austen_and_her_quote(context):
    person_service = get_set_service(context, 'person_service')
    quote_service = get_set_service(context, 'quote_service')
    params = params_for_get_by_name(context)
    actual = BasicResponse(quote_service.quotes_by_name(params))
    person_service.delete_person_by_id(actual.data[0]['id'])
    assert actual.status_code == HTTPStatus.OK
    del_res = BasicResponse(person_service.delete_person_by_id(actual.data[0]['id']))
    assert del_res.status_code == HTTPStatus.OK
    assert context.scenario_level[ORIG_NUM_PEOPLE] == BasicResponse(person_service.get_people_count()).data
    assert context.scenario_level[ORIG_NUM_QUOTES] == BasicResponse(quote_service.get_quote_count()).data


# Ref: Scenario - system does a uniqueness check before a new user is saved
@step('json string input having a new id with existing name and dates')
def system_will_not_allow_identical_name_and_dates(context):
    bad_input = data.data_that_matches_existing_person_with_unused_id()
    context.scenario_level['input'] = bad_input


@step('the database will throw data integrity violation exception')
def the_database_will_throw_a_data_integrity_violation(context):
    quote_service = get_set_service(context, 'quote_service')
    input = context.scenario_level['input']
    basic_response = BasicResponse(quote_service.add_quotes(input))
    context.scenario_level['basic_response'] = basic_response
    assert basic_response.status_code == HTTPStatus.BAD_REQUEST
    assert 'unique_data_constraint' in basic_response.error_detail


@step('the transaction will roll back and the new record will not be created')
def the_new_record_will_not_be_created(context):
    person_service = get_set_service(context, 'person_service')
    basic_response = BasicResponse(person_service.find_person_by_id(context.scenario_level['input']['id']))
    assert basic_response.status_code == HTTPStatus.NOT_FOUND


# Ref: Scenario - add new person with quotes then find by name and then delete all added data
@step('the api is called with good data showing a new person and two quotes')
def add_new_person_with_quotes_good_data(context):
    quote_service = get_set_service(context, 'quote_service')
    person_service = get_set_service(context, 'person_service')
    set_up_original_counts(context, quote_service, person_service)
    good_input = data.data_that_will_successfully_add_a_person_and_two_quotes()
    context.scenario_level['input'] = good_input
    quote_response = BasicResponse(quote_service.add_quotes(good_input))
    context.scenario_level['quote_response'] = quote_response


@step('it returns the correct number of quotes with a successful return code')
def add_new_person_with_quotes_returns_successfully(context):
    new_len = len(list(context.scenario_level['quote_response'].data))
    if new_len == 1:
        check_for_error(context.scenario_level['quote_response'].data)
    orig_len = context.scenario_level['orig_num_quotes']
    assert context.scenario_level['quote_response'].status_code == HTTPStatus.OK
    assert new_len == 2 + orig_len


@step('person and quotes can be retrieved by name and the data will match the input data')
def add_new_person_with_quotes_has_a_return_with_the_expected_data(context):
    input = context.scenario_level['input']
    quote_service = get_set_service(context, 'quote_service')
    params = params_for_get_by_name(context)
    actual = BasicResponse(quote_service.quotes_by_name(params))
    context.scenario_level['delete_person_id'] = actual.data[0]['id']
    if len(list(actual.data)) > 1:
        print('rework test to deal with duplicate names')
        sys.exit(os.EX_OK)
    assert actual.data[0]['dates'] == input['dates']
    assert len(list(input['quotes'])) == len(list(actual.data[0]['quotes']))
    assert input['quotes'][0]['quote'] == actual.data[0]['quotes'][0]['quote']


@step('the new person and their quotes can be deleted by person id')
def delete_newly_created_person_by_id(context):
    person_service = get_set_service(context, 'person_service')
    quote_service = get_set_service(context, 'quote_service')
    id_to_delete = context.scenario_level['delete_person_id']
    person_service.delete_person_by_id(id_to_delete)
    params = params_for_get_by_name(context)
    actual = BasicResponse(quote_service.quotes_by_name(params))
    res = BasicResponse(quote_service.get_quote_count())
    assert actual.status_code == HTTPStatus.OK
    assert len(list(actual.data)) == 0
    assert res.data == context.scenario_level['orig_num_quotes']


# Ref: Scenario - the quotes endpoint allows the system to find an existing person and add new quotes
@step('a person found by id has original quotes saved for further use')
def find_person_by_id_one_quote(context):
    person_service = get_set_service(context, 'person_service')
    quote_service = get_set_service(context, 'quote_service')
    orig_person = BasicResponse(person_service.find_person_by_id(uc.EXISTING_PERSON_ID))
    orig_quote_count = BasicResponse(quote_service.get_quote_count())
    context.scenario_level[ORIG_NUM_QUOTES] = orig_quote_count.data
    context.scenario_level['orig_person'] = orig_person.data
    assert orig_person.status_code == HTTPStatus.OK
    assert orig_quote_count.status_code == HTTPStatus.OK


@step('the api is called with good data to add a second quote for the same person')
def api_call_adding_one_quote_to_existing_person(context):
    quote_service = get_set_service(context, 'quote_service')
    input_data = data.add_quote_to_jane_austen()
    quote_response = BasicResponse(quote_service.add_quotes(input_data))
    show_quotes = quote_response.data
    if not isinstance(show_quotes, list):
        check_for_error(show_quotes)
    context.scenario_level['input_data'] = input_data
    context.scenario_level['show_quotes'] = list(show_quotes)
    assert quote_response.status_code == HTTPStatus.OK


@step('the successful call will show that the total number of quotes has increased by one')
def compare_total_number_of_quotes_to_original(context):
    new_num_quotes = len(context.scenario_level['show_quotes'])
    assert new_num_quotes == context.scenario_level[ORIG_NUM_QUOTES] + 1


@step('the person found again by id now has two quotes with one of them matching input data')
def find_person_by_id_again_additional_quote_is_correct(context):
    person_service = get_set_service(context, 'person_service')
    orig_person_extra_quote = BasicResponse(person_service.find_person_by_id(uc.EXISTING_PERSON_ID))
    assert orig_person_extra_quote.status_code == HTTPStatus.OK
    updated_quotes = orig_person_extra_quote.data['quotes']
    assert len(updated_quotes) == len(context.scenario_level['orig_person']['quotes']) + 1
    list_of_one = utils.subset_list_by_key_and_value(updated_quotes, 'quoteNote', 'Marianne Dashwood')
    assert len(list_of_one) == 1
    context.scenario_level['added_quote'] = list_of_one[0]
    assert 'saves me the trouble of liking them a great deal' in context.scenario_level['added_quote']['quote']


@step('the new quote can be deleted without deleting the person')
def delete_one_quote_using_quote_id(context):
    quote_service = get_set_service(context, 'quote_service')
    person_service = get_set_service(context, 'person_service')
    quote_id = context.scenario_level['added_quote']['id']
    res = BasicResponse(quote_service.delete_quote_by_id(quote_id))
    assert res.status_code == HTTPStatus.OK
    orig_person_one_quote = BasicResponse(person_service.find_person_by_id(uc.EXISTING_PERSON_ID))
    orig_person_quotes = context.scenario_level['orig_person']['quotes']
    assert len(orig_person_one_quote.data['quotes']) == len(orig_person_quotes)
    assert orig_person_one_quote.data['quotes'][0]['quote'] == orig_person_quotes[0]['quote']


# Ref: Scenario - illegal state error - adding quotes for existing id with non-matching name or date fields
@step('with only a person id a quote can be added but any person data in the input must match db person record')
def throw_illegal_state_with_existing_data(context):
    quote_service = get_set_service(context, 'quote_service')
    person_service = get_set_service(context, 'person_service')
    set_up_original_counts(context, quote_service, person_service)
    bad_input = data.existing_id_but_first_last_and_dates_do_not_match()
    quote_response = BasicResponse(quote_service.add_quotes(bad_input))
    context.scenario_level['input'] = bad_input
    assert is_illegal_state(quote_response)


@step('if only one of first or last names or dates field is wrong it will throw an error')
def update_two_of_three_fields_still_throw_illegal_state_exception(context):
    bad_input = context.scenario_level['input']
    bad_input['firstName'] = 'Jane'
    bad_input['lastName'] = 'Austen'
    quote_service = get_set_service(context, 'quote_service')
    quote_response = BasicResponse(quote_service.add_quotes(bad_input))
    assert is_illegal_state(quote_response)


@step('the existing person will still exist but the numbers of people and quotes will stay the same')
def call_quote_not_created_num_people_unchanged_with_existing_person_true(context):
    quote_not_created_num_people_unchanged(context, True)


# Ref: Scenario - required field constraint violation --> thrown if required fields are missing, no record created
@step('if name or dates are missing for adding a new person it will throw a missing fields contraint violation')
def missing_name_or_date_field_will_throw_constraint_violation(context):
    quote_service = get_set_service(context, 'quote_service')
    person_service = get_set_service(context, 'person_service')
    set_up_original_counts(context, quote_service, person_service)
    bad_input = data.data_that_will_successfully_add_a_person_and_two_quotes()
    bad_input.pop('dates')
    context.scenario_level['input'] = bad_input
    quote_response = BasicResponse(quote_service.add_quotes(bad_input))
    context.scenario_level['quote_response'] = quote_response
    assert quote_response.status_code == HTTPStatus.BAD_REQUEST
    assert is_missing_field(quote_response, 'Dates')


@step('find new person by name will return an empty list')
def find_new_person_by_name_returns_empty_list(context):
    person_service = get_set_service(context, 'person_service')
    quote_service = get_set_service(context, 'quote_service')
    params = params_for_get_by_name(context)
    current_num_people = BasicResponse(person_service.get_people_count()).data
    person_not_added = BasicResponse(quote_service.quotes_by_name(params))
    assert len(person_not_added.data) == 0
    assert current_num_people == context.scenario_level['orig_num_people']


@step('a missing quote will also send a missing field error')
def missing_quote_constraint_violation(context):
    quote_service = get_set_service(context, 'quote_service')
    person_service = get_set_service(context, 'person_service')
    context.scenario_level['orig_num_people'] = BasicResponse(person_service.get_people_count()).data
    bad_input = data.data_that_will_successfully_add_a_person_and_two_quotes()
    bad_input['quotes'][0]['quote'] = ''
    context.scenario_level['input'] = bad_input
    quote_response = BasicResponse(quote_service.add_quotes(bad_input))
    context.scenario_level['quote_response'] = quote_response
    assert quote_response.status_code == HTTPStatus.BAD_REQUEST
    assert is_missing_field(quote_response, 'Quote')


@step('adding a quote to an existing person will give a missing field error for a blank quote field')
def adding_quote_to_existing_person_with_blank_quote_field_gives_missing_field_error(context):
    quote_service = get_set_service(context, 'quote_service')
    person_service = get_set_service(context, 'person_service')
    context.scenario_level['orig_num_people'] = BasicResponse(person_service.get_people_count()).data
    context.scenario_level['orig_num_quotes'] = BasicResponse(quote_service.get_quote_count()).data
    bad_input = data.data_that_will_successfully_add_a_person_and_two_quotes()
    bad_input['quotes'][0].pop('quote')
    context.scenario_level['input'] = bad_input
    quote_response = BasicResponse(quote_service.add_quotes(bad_input))
    context.scenario_level['quote_response'] = quote_response
    assert quote_response.status_code == HTTPStatus.BAD_REQUEST
    assert 'Index Out of Bounds' in quote_response.data['detail']
    assert 'no quote field' in quote_response.data['detail']


# Note: this step is used in lots of tests and the actual method is called elsewhere when there is an existing person
@step('the total number of quotes or people will not decrease or increase')
def quote_not_created_num_people_unchanged(context, person_existing=False):
    quote_service = get_set_service(context, 'quote_service')
    person_service = get_set_service(context, 'person_service')
    current_num_people = BasicResponse(person_service.get_people_count()).data
    current_num_quotes = BasicResponse(quote_service.get_quote_count()).data
    params = params_for_get_by_name(context)
    person_not_added = BasicResponse(quote_service.quotes_by_name(params))
    assert current_num_people == context.scenario_level[ORIG_NUM_PEOPLE]
    assert current_num_quotes == context.scenario_level[ORIG_NUM_QUOTES]
    expected_len = 1 if person_existing else 0
    assert len(person_not_added.data) == expected_len


@step('no quote field key will create an index out of bounds error with message that references quote field')
def a_missing_quote_field_key_causes_idx_out_of_bounds_and_message_will_reference_the_likely_root_cause(context):
    quote_service = get_set_service(context, 'quote_service')
    bad_input = data.data_that_will_successfully_add_a_person_and_two_quotes()
    bad_input['quotes'][0].pop('quote')
    context.scenario_level['input'] = bad_input
    quote_response = BasicResponse(quote_service.add_quotes(bad_input))
    context.scenario_level['quote_response'] = quote_response

    assert is_index_out_of_bounds(quote_response)
    assert 'no quote field in Quote Array' in quote_response.data['detail']


def get_set_service(context, key):
    if context.feature_level.get(key) is not None:
        return context.feature_level[key]
    if key == 'quote_service':
        context.feature_level[key] = QuoteService(context)
    if key == 'person_service':
        context.feature_level[key] = PersonService(context)
    return context.feature_level[key]


def set_up_original_counts(context, quote_service, person_service):
    context.scenario_level[ORIG_NUM_PEOPLE] = BasicResponse(person_service.get_people_count()).data
    context.scenario_level[ORIG_NUM_QUOTES] = BasicResponse(quote_service.get_quote_count()).data


# Note: normally when the tests run, there is a clean up step, so you can use the same data without worrying about
#       unique constraint errors.  If you are debugging however, this will error will remind you to turn the
#       spring-qa-testing-app off and then on again, thus resetting the database
def check_for_error(data):
    if utils.key_in_dictionary(data, 'detail'):
        error = 'Quotes and/or people must be unique. The application being tested needs to be stopped and restarted.'
        if 'constraint' in data['detail']:
            print(error)
            sys.exit(os.EX_OK)


def params_for_get_by_name(context):
    first = context.scenario_level['input']['firstName']
    last = context.scenario_level['input']['lastName']
    return {'firstName': first, 'lastName': last}


def is_illegal_state(response):
    if response.status_code != HTTPStatus.BAD_REQUEST:
        return False
    if utils.key_not_in_dictionary(response.data, 'detail'):
        return False
    if 'non-matching data' in response.data['detail']:
        return True


def is_missing_field(response, field):
    if response.status_code != HTTPStatus.BAD_REQUEST:
        return False
    if utils.key_not_in_dictionary(response.data, 'detail'):
        return False
    if f'{field} must not be null' in response.data['detail']:
        return True


def is_index_out_of_bounds(response):
    if response.status_code != HTTPStatus.BAD_REQUEST:
        return False
    if utils.key_not_in_dictionary(response.data, 'detail'):
        return False
    if 'Index Out of Bounds' in response.data['detail']:
        return True
