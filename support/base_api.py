# common to all services
from abc import ABC, abstractmethod
import requests
import constants.environment_keys as ek

requests.packages.urllib3.disable_warnings()


class BaseApi(ABC):
    def __init__(self):
        self.method = ''
        self.data = {}
        self.url = ''
        self.headers = {}
        self.params = {}
        self.environment = {}

    def send(self):
        if self.environment[ek.SEND_VERIFY_FALSE]:
            return self.send_verify_false()
        return self.send_no_verify()

    def send_verify_false(self):
        if self.method == 'get':
            return requests.get(self.url, verify=False, headers=self.headers, params=self.params)
        if self.method == 'uaa':
            return requests.post(self.url, verify=False, headers=self.headers, data=self.data)
        if self.method == 'post':
            return requests.post(self.url, verify=False, headers=self.headers, json=self.data, params=self.params)
        if self.method == 'put':
            return requests.put(self.url, verify=False, headers=self.headers, json=self.data, params=self.params)
        if self.method == 'delete':
            return requests.delete(self.url, verify=False, headers=self.headers, params=self.params)
        if self.method == 'patch':
            return requests.patch(self.url, verify=False, headers=self.headers, json=self.data, params=self.params)
        else:
            return None

    def send_no_verify(self):
        if self.method == 'get':
            return requests.get(self.url, headers=self.headers, params=self.params)
        if self.method == 'post':
            return requests.post(self.url, headers=self.headers, json=self.data, params=self.params)
        if self.method == 'put':
            return requests.put(self.url, headers=self.headers, json=self.data, params=self.params)
        if self.method == 'delete':
            return requests.delete(self.url, headers=self.headers, params=self.params)
        if self.method == 'patch':
            return requests.patch(self.url, headers=self.headers, json=self.data, params=self.params)
        if self.method == 'uaa':
            return requests.post(self.url, headers=self.headers, data=self.data)
        else:
            return None

    @abstractmethod
    def set_headers(self, kwargs):
        ''' create and set header. '''

    @abstractmethod
    def set_url(self, kwargs):
        ''' create and set url '''
