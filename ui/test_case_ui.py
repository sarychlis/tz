import string
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class TestCaseUi(unittest.TestCase):

    def setUp(self):
        s = Service('./chromedriver')
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    @staticmethod
    def getTestUrl(path) -> string:
        return 'http://httpbin.org/' + path
