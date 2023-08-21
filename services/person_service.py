from support.base_api import BaseApi
import constants.environment_keys as ek


class PersonService(BaseApi):

    def __init__(self, context):
        # __init__ different from the base class
        super().__init__()
        self.environment = context.environment
        # leaving base_route (below) here, since it makes sense for microservices
        # Empty string, because the quote service has a different base route for each endpoint
        self.base_route = ''
        self.set_headers()

    def get_people_count(self):
        self.method = 'get'
        route = 'people_count'
        self.set_url(route)
        return self.send()

    def get_show_people_quotes(self):
        self.method = 'get'
        route = 'show'
        self.set_url(route)
        return self.send()

    def find_person_by_id(self, id):
        self.method = 'get'
        route = f'person/{id}'
        self.set_url(route)
        return self.send()

    def delete_person_by_id(self, id):
        self.method = 'delete'
        route = f'person/{id}'
        self.set_url(route)
        return self.send()

    def set_headers(self, content_type='application/json'):
        self.headers = {
            'Content-Type': content_type
        }

    def set_url(self, route):
        self.url = f'{self.environment[ek.BASE_URL]}/{self.base_route}{route}'
