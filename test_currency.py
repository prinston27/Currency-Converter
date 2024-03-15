from cmath import nan
import unittest
from currency import CurrencyConverter

class TestCurrencyConverterInstantiation(unittest.TestCase):
    """
    Class used for testing the instanciation of the CurrencyConverter class from currency.py
    """
    def test_correct_from_currency(self):
        obj = CurrencyConverter('GBP','AUD','2022-01-05')
        self.assertEqual(obj.from_currency,'GBP',"Incorrect Currency")
        
        
    def test_correct_to_currency(self):
        obj = CurrencyConverter('GBP','AUD','2022-01-05')
        self.assertEqual(obj.to_currency,'AUD',"Incorrect Currency")
    
    def test_correct_date(self):
        obj = CurrencyConverter('GBP','AUD','2022-01-05')
        self.assertEqual(obj.date_input,'2022-01-05',"Invalid Date")

    def test_incorrect_from_currency(self):
        obj = CurrencyConverter('ADD','GGG','2022-45-13')
        self.assertEqual(obj.from_currency,'ADD',"Correct Currency")

    def test_incorrect_to_currency(self):
        obj = CurrencyConverter('ADD','GGG','2022-45-13')
        self.assertEqual(obj.to_currency,'GGG',"Correct Currency")

    def test_incorrect_date(self):
        obj = CurrencyConverter('ADD','GGG','2022-45-13')
        self.assertEqual(obj.date_input,'2022-45-13',"Correct Date")


class TestCurrencyCheck(unittest.TestCase): 
    """
    Class used for testing the CurrencyConverter.check_currencies() method from currency.py
    """

    def test_incorrect_currencies(self):
        obj = CurrencyConverter('GBB','ADD','2022-06-10')
        with self.assertRaises(SystemExit) as cm:
            obj.check_currencies()
            self.assertEqual(cm.exception, 10)

class TestReverseRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.reverse_rate() method from currency.py
    """

    def test_invalid_inverse_rate(self):
        obj = CurrencyConverter('GBP','AUD','2022-01-01')
        obj.inverse_rate = -67
        with self.assertRaises(SystemExit) as cm:
            obj.reverse_rate()
            self.assertEqual(cm.exception,10)
    
    def test_valid_inverse_rate(self):
        obj = CurrencyConverter('GBP','AUD','2022-01-01')
        obj.inverse_rate = 67
        self.assertEqual(obj.reverse_rate(),67,'Correct Inverse Rate')
        
    
class TestRoundRate(unittest.TestCase): 
    """
    Class used for testing the CurrencyConverter.round_rate() method from currency.py
    """
    def test_invalid_rate(self):
        obj = CurrencyConverter('GBP','AUD','2022-01-01')
        with self.assertRaises(SystemExit) as cm:
            obj.round_rate(-67)
            self.assertEqual(cm.exception,10)

    def test_valid_rate(self):
        obj = CurrencyConverter('GBP','AUD','2022-01-01')
        self.assertEqual(obj.round_rate(67),67,'Correct Inverse Rate')


        

class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.get_historical_rate() method from currency.py
    """
    
    def test_succesful_connection(self):
        obj = CurrencyConverter('AUD','GBP','2022-01-01')
        self.assertTrue(obj.get_historical_rate())

    def test_unsuccessful_connection(self):
        obj = CurrencyConverter('ADD','GP','2021-01-01')
        with self.assertRaises(SystemExit) as cm:
            obj.get_historical_rate()
            self.assertEqual(cm.exception,10)
    
if __name__ == '__main__':
    unittest.main()