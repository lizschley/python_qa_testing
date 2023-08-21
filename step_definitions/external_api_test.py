from behave import step
from services.example_external_service import ExampleExternalService
from support.basic_response import BasicResponse
from http import HTTPStatus
import utilities.utils as utils


LOCATION_ID = '38.02632365748759-78.48496767659267'

UPPERMOST_RADIUS = 100
UPPERMOST_LIMIT = 10

PARAMS = {
    'location_id': LOCATION_ID,
    'radius': UPPERMOST_RADIUS,
    'limit': UPPERMOST_LIMIT
}

# Ref: Scenario Outline - Maximum allowed Radius and Limit along with a minimum population of 100,000 gives you Richmond
@step('you use the maximum of both radius and limit and a Charlottesville location id')
def using_maximum_allowed_radius_and_limit_and_charlottesville_location_id(context):
    new_service = ExampleExternalService(context)
    assert utils.key_in_dictionary(new_service.headers, 'X-RapidAPI-Key')
    assert utils.key_in_dictionary(new_service.headers, 'X-RapidAPI-Host')
    assert 'nearbyCities' == new_service.base_route
    context.feature_level['service'] = new_service


@step('you can get Richmond in the result if you use a minimum population of 100000')
def run_rapidapi_and_check_results(context):
    service = context.feature_level['service']
    params = PARAMS
    params['min_pop'] = 100000
    response = BasicResponse(service.get_nearby_cities(params))
    response.write_to_file('richmond', folder='example')
    assert response.status_code == HTTPStatus.OK
    results = response.data['data']
    assert len(results) == UPPERMOST_LIMIT
    look_for = utils.find_dict_from_list_by_key_and_value(results, 'city', 'Richmond')
    assert look_for['distance'] == 66.35
    assert look_for['countryCode'] == 'US'
    assert look_for['regionCode'] == 'VA'
