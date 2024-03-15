import unittest
from checks import check_arguments, check_date


class TestCheckArguments(unittest.TestCase):
    """
    Class used for testing the check_arguments() function from checks.py
    """
    def test_no_Arguments(self):
        with self.assertRaises(SystemExit) as cm:
            check_arguments([])
            self.assertEqual(cm.exception, 10)

    def test_one_Argument(self):
        with self.assertRaises(SystemExit) as cm:
            check_arguments(['2022-01-01'])
            self.assertEqual(cm.exception, 10)    

    def test_two_Arguments(self):
        with self.assertRaises(SystemExit) as cm:
            check_arguments(['2022-01-01','AUD'])
            self.assertEqual(cm.exception, 10)

    def test_three_Arguments(self):
        #check_arguments(['2022-01-01','AUD','GBP'])
        self.assertEqual(check_arguments(['2022-01-01','AUD','GBP']),['2022-01-01','AUD','GBP'],'Incorrect Arguments')
        
class TestCheckDate(unittest.TestCase):
    """
    Class used for testing the check_date() function from checks.py
    """
    def test_FailDateValidation1(self):
        with self.assertRaises(SystemExit) as cm:
            check_date('2022-43-45')
            self.assertEqual(cm.exception, 10)
 
    def test_SuccessDateValidation(self):
        self.assertTrue(check_date('2022-01-01'))
        

if __name__ == '__main__':
    unittest.main()