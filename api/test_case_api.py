import string
import unittest

import requests
from requests import Response


class TestCaseApi(unittest.TestCase):

    @staticmethod
    def getBaseUrl() -> string:
        return 'http://httpbin.org/'

    def makeGetRequest(self, path) -> Response:
        return requests.get(self.getBaseUrl() + path)

