import datetime
import sys

def check_arguments(args):
    """
    Function that will check if there are enough input arguments provided (ie exactly 3) and will return the input arguments if it is the case.
    Otherwise the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    # => Input Arguments

    Pseudo-code
    ----------
    # => if length of arguments is not equal to 3
            print Error!You need to provide 3 arguments in the following order: <date> <currency1> <currency2>

    Returns
    -------
    # => Returns Error Message if length is not equal to 3
    
    """
    if len(args) != 3:
        print("ERROR!!You need to provide 3 arguments in the following order: <date> <currency1> <currency2>")
        sys.exit(10)
    return args
    

def check_date(date_input):
    """
    Function that will check if the provided date is valid and will return the value True if that is the case. 
    Otherwise the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    # => Date argument

    Pseudo-code
    ----------
    # => try
            check if date is in the accepted format using strptime
            Then check if the date is after 2000-01-01
            if error
                return 'Provided date is invalid"

    Returns
    -------
    # => Returns "Provided date is invalid" if date format is invalid
    """
    from datetime import datetime, date
    date_value = date_input
    try:
        accepted_date = datetime.strptime(date_value, '%Y-%m-%d').date()
        if not (date(2000, 1, 1) <= accepted_date):
            raise ValueError('Date out of range')
        else:
            return True
    except ValueError:
        print('Provided date is invalid')
        sys.exit(10)