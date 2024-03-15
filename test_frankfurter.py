import unittest
from frankfurter import Frankfurter
import requests
class TestUrl(unittest.TestCase):
    """
    Class used for testing the url attributes of the Frankfurter class from checks.py
    """
    def test_correct_base_url(self):
        obj = Frankfurter()
        self.assertEqual(str(obj.base_url),'https://www.frankfurter.app/')
    
    def test_correct_currencies_url(self):
        obj = Frankfurter()
        self.assertEqual(str(obj.currencies_url),'https://api.frankfurter.app/currencies')
    
    def test_correct_historical_url(self):
        obj = Frankfurter()
        self.assertEqual(str(obj.historical_url),'https://www.frankfurter.app/')
    

class TestCurrenciesList(unittest.TestCase):
    """
    Class used for testing the currencies attribute of the Frankfurter class from checks.py
    """
    response=requests.get("https://www.frankfurter.app/currencies")
    list=response.json()
    frank_obj=Frankfurter()
    def test_currency_list(self):
        self.assertEqual(self.frank_obj.currencies,self.list,"Incorrect currency list")
        

class TestCheckCurrency(unittest.TestCase):
    """
    Class used for testing the Frankfurter.check_currency() method from frankfurter.py
    """
    def test_correct_currency(self):
        obj = Frankfurter()
        self.assertTrue(obj.check_currency('AUD'),'Incorrect Currency')

    def test_incorect_currency(self):
        obj = Frankfurter()
        self.assertFalse(obj.check_currency('ADD'),'Correct Currency') 
    

class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the Frankfurter.get_historical_rate() method from frankfurter.py
    """
    def test_successful_get_rates(self):
        obj = Frankfurter()
        
        self.assertTrue(obj.get_historical_rate('AUD','GBP','2022-01-02'))

    def test_unsuccessful_get_rates(self):
        obj = Frankfurter()
        with self.assertRaises(SystemExit) as cm:
            self.assertFalse(obj.get_historical_rate('ADD','GBB','2022-01-67'))
            self.assertEqual(cm.exception, 10)


        
    
if __name__ == '__main__':
    unittest.main()