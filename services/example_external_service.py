from support.base_api import BaseApi
import constants.environment_keys as ek


class ExampleExternalService(BaseApi):

    def __init__(self, context):
        # __init__ different from the base class
        super().__init__()
        self.environment = context.environment
        self.base_route = 'nearbyCities'
        self.set_headers()

    def get_nearby_cities(self, params):
        self.method = 'get'
        location_id = params['location_id']
        route = f'?radius={params["radius"]}&minPopulation={params["min_pop"]}&limit={params["limit"]}'
        self.set_url(location_id, route)
        return self.send()

    def set_headers(self, content_type='application/json'):
        self.headers = {
            'Content-Type': content_type,
            ek.RAPID_API_HOST_VAR: ek.RAPID_API_HOST,
            ek.RAPID_API_KEY_VAR: ek.RAPID_API_KEY
        }

    def set_url(self, location_id, route):
        self.url = f'{self.environment[ek.RAPID_API_BASE_URL]}/{location_id}/{self.base_route}{route}'
