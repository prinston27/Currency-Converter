from urllib import response
from api import call_get
import sys

class Frankfurter:
    """
    Class that manages API calls to Frankfurter. It will be used to store the URLS to the relevant endpoints. It will also automatically call the Currencies endpoint and store the return list of available currency codes.

    Attributes
    ----------
    base_url : str
        Base url to Frankfurter API
    currencies_url : str
        Frankfurter endpoint for extracting currencies list
    historical_url : str
        Frankfurter endpoint for extracting historical currencies conversion rates
    currencies: list
        List of available currency codes
    """
    def __init__(self):
        self.base_url = "https://www.frankfurter.app/"
        self.currencies_url = "https://api.frankfurter.app/currencies"
        self.historical_url = "https://www.frankfurter.app/"
        self.currencies=self.get_currencies_list()

    def get_currencies_list(self):
        """
        Method that will get the list of available currencies and returns it as a Python list.

        Parameters
        ----------
        # => To be filled by student

        Pseudo-code
        ----------
        # => To be filled by student

        Returns
        -------
        # => To be filled by student
        """
        
        currency_list = call_get(self.currencies_url).json()
        return currency_list

    def check_currency(self, currency):
        """
        Method that will check if a provided currency code is valid and return True if that is the case.
        Otherwise it will return False.

        Parameters
        ----------
        # => Currency

        Pseudo-code
        ----------
        # => if currency not in currency_list
                return False
              else
                return True

        Returns
        -------
        # => Returns Boolean values
        """
        
        currency_list = self.get_currencies_list()
        if currency not in currency_list:
            return False
        else:
            return True

    def get_historical_rate(self, from_currency, to_currency, from_date, amount=1):
        """
        Method that will call the historical API endpoint in order to get the conversion rate for a given dates and currencies. It will return an requests.models.Response object.

        Parameters
        ----------
        # => From_date = Date for which we'd require the historical rate
        #   from_currency = currency from which we'll need to convert
            to_currency = currency to which we'll need to convert
            amount = base value

        Pseudo-code
        ----------
        # => use call_get to fetch the historical rate
            return historical rate

        Returns
        -------
        # => Returns the historical rate
        """
        try:
            response = call_get(self.historical_url+f'{from_date}?to={to_currency},{from_currency}').json()
            historical_rate = response.get("rates")
        except:
            sys.exit(10)
        else:
            return historical_rate
