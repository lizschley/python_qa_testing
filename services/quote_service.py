from support.base_api import BaseApi
import constants.environment_keys as ek


class QuoteService(BaseApi):

    def __init__(self, context):
        # __init__ different from the base class
        super().__init__()
        self.environment = context.environment
        # leaving base_route here, since it made sense for microservices
        # Empty string, because the quote service has a different base url for each endpoint
        self.base_route = ''
        self.set_headers()

    def get_quote_count(self):
        self.method = 'get'
        route = 'quote_count'
        self.set_url(route)
        return self.send()

    def get_show_people_quotes(self):
        self.method = 'get'
        route = 'show'
        self.set_url(route)
        return self.send()

    def add_quotes(self, payload):
        self.method = 'post'
        self.data = payload
        route = 'quotes'
        self.set_url(route)
        return self.send()

    def quotes_by_name(self, params):
        self.method = 'get'
        first = params.get('firstName')
        last = params.get('lastName')
        route = 'quotesByName?firstName=' + first + '&lastName=' + last
        self.set_url(route)
        return self.send()

    def delete_quote_by_id(self, id):
        self.method = 'delete'
        route = f'quote/{id}'
        self.set_url(route)
        return self.send()

    def set_headers(self, content_type='application/json'):
        self.headers = {
            'Content-Type': content_type
        }

    def set_url(self, route):
        self.url = f'{self.environment[ek.BASE_URL]}/{self.base_route}{route}'
