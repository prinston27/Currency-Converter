import sys
from frankfurter import Frankfurter

class CurrencyConverter:
    """
    Class that represents a Currency conversion object. It will be used to store the input arguments (currency codes, date) and also other information required (amount, rate, inverse rate, instantiation of Frankfurter class).

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
    api : Frankfurter
        Instance of Frankfurter class
    """
    def __init__(self, from_currency, to_currency, date_input):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.date_input = date_input

    def check_currencies(self):
        """
        Method that will check if currency codes stored in the class attributes are valid.
        Otherwise the program will exit and display the relevant message provided in the assignment brief

        Parameters
        ----------
        # => None

        Pseudo-code
        ----------
        # => Create object of class Frankfurter
            fetch currency_list using get_currency_list function
            initialize count to 0
            if from_currency does not exist in currency_list
                print "from_currency is not a valid currency code"
                increment count by 1
                sys.exit()
            if to_currency does not exist in currency_list
                print "to_currency is not a valid currency code"
                increment count by 1
                sys.exit()
            if count == 2
                print "from_currency and to_currency are not valid currency codes"
                sys.exit()
        Returns
        -------
        # => Returns whether input currencies are valid or not  
        """
        frank = Frankfurter()
        currency_list = frank.get_currencies_list()
        count = 0

        if not frank.check_currency(self.from_currency):
             print(f"{self.from_currency} is not a valid currency code")
             count+=1
            
        if not frank.check_currency(self.to_currency):
            print(f"{self.to_currency} is not a valid currency code")
            count+=1
        
        if count == 2:
            print(f"{self.from_currency} and {self.to_currency} are not valid currency codes")
            sys.exit(10)
        
    def reverse_rate(self):
        """
        Method that will calculate the inverse rate from the value stored in the class attribute, round it to 4 decimal places and save it back in the class attribute inverse_rate.

        Parameters
        ----------
        # => None

        Pseudo-code
        ----------
        # => round inverse_rate to 4 decimal places
            return inverse_rate

        Returns
        -------
        # => returns inverse_rate rounded to 4 decimal places
        """
        if(self.inverse_rate<0):
            sys.exit(10)    
        self.inverse_rate = round(self.inverse_rate,4)
        return self.inverse_rate

    def round_rate(self, rate):
        """
        Method that will round an input argument to 4 decimals places.

        Parameters
        ----------
        # => Rate 

        Pseudo-code
        ----------
        # => return rate rounded to 4 decimal places

        Returns
        -------
        # => return rate rounded to 4 decimal places
        """

        if (rate<0):
            sys.exit(10)
        return round(rate,4)

    def get_historical_rate(self):
        """
        Method that will call the Frankfurter API and get the historical conversion rate for the currencies (rounded to 4 decimals) and date stored in the class attributes.
        Then it will calculate the inverse rate and will exit by displaying the relevant message provided in the assignment brief

        Parameters
        ----------
        # => None

        Pseudo-code
        ----------
        # => create an object of class Frankfurter
            fetch historical rate from get_historical_rate() of Frankfurter class
            
            conversion_rate equals to_currency/from_currency
            inverse_rate equals from_currency/to_currency
            
            call function round_rate 
            call function reverse_rate

            

        Returns
        -------
        # => print("The conversion rate on {self.date_input} from {self.from_currency} to {self.to_currency} was {self.conversion_rate}. The inverse rate was {self.inverse_rate})"
        """
        try:
            frank = Frankfurter()
        
            historical_rate = frank.get_historical_rate(self.from_currency,self.to_currency,self.date_input)

            self.conversion_rate = (historical_rate[self.to_currency]/historical_rate[self.from_currency])
            self.inverse_rate = (historical_rate[self.from_currency]/historical_rate[self.to_currency])

            self.conversion_rate = self.round_rate(self.conversion_rate)
            self.reverse_rate()

            print(f"The conversion rate on {self.date_input} from {self.from_currency} to {self.to_currency} was {self.conversion_rate}. The inverse rate was {self.inverse_rate}")
        
            return True
        except:
            sys.exit(10)
        
        
        



        