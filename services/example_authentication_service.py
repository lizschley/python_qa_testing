# basic authentication
import os
from support.base_api import BaseApi
import constants.environment_keys as ek


class ExampleAuthenticationService(BaseApi):

    def __init__(self, context):
        # __init__ different from the base class
        super().__init__()
        # self.base_route = 'uaa'
        # self.set_headers()
        # data = f'username={os.getenv("AUTH_USERNAME")}&password={os.getenv("AUTH_PASSWORD")}&grant_type=password'
        # self.data = data
        self.environment = context.environment

    def get_credentials(self):
        # self.method = 'uaa'
        # self.set_url('oauth/token')
        # res = self.send()
        # return res.json()[ek.ACCESS_TOKEN]
        return 'no access token needed for this environment'

    def set_headers(self):
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Basic {os.getenv("AUTH_SECRET")}'
        }

    def set_url(self, route):
        self.url = f'{self.environment[ek.BASE_URL]}/{self.base_route}/{route}'
