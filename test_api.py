import requests
import unittest
from api import call_get
import sys

class TestAPI(unittest.TestCase):
    """
    Class used for testing the call_get() function in api.py
    """

    def test_successful_connection(self):
        self.assertEqual(str(call_get("https://www.frankfurter.app/")), '<Response [200]>','Incorrect url')

    def test_unsuccessful_connection(self):
        self.assertEqual(str(call_get("https://www.frankfurterXYZ.app/")), "There is an error with Frankfurter API",'Correct url')
    
if __name__ == '__main__':
    unittest.main()
