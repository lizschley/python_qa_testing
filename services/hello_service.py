from support.base_api import BaseApi
import constants.environment_keys as ek


class HelloService(BaseApi):

    def __init__(self, context):
        # __init__ different from the base class
        super().__init__()
        self.environment = context.environment
        # the base route is useful for microservices, example of usage in set_url below
        # the spring-qa-testing app, does have micro-services, and a common base_route is not used
        self.base_route = 'hello'
        # a standard way to authenticate
        # self.set_headers(self.environment[ek.ACCESS_TOKEN])
        self.set_headers()

    def hello_world(self, params):
        self.method = 'get'
        param = params.get('name')
        route = '?name=' + param if param else ''
        self.set_url(route)
        return self.send()

    def set_headers(self):
        self.headers = {
            # this is where to put the access token (must pass in, see init above)
            # 'Authorization': f'Bearer {access_token}',
            'Content-Type': 'text/plain'
        }

    def set_url(self, route):
        self.url = f'{self.environment[ek.BASE_URL]}/{self.base_route}{route}'
