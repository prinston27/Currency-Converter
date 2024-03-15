import requests
import sys

def call_get(url: str) -> requests.models.Response:
    """
    Function that will call the API endpoint (input parameter) and return its response as a requests.models.Response object
    In case of an error, the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    Frankfurter API URL

    Pseudo-code
    ----------
        Establish connection with URL
         If connection succesful 
            return response
         else
            return "There is an error with Franfurter API"

    Returns
    -------
    Return response if connection successful. Else returns error message.
    """
    
    # => To be filled by student
    try:
        resp = requests.get(url)
    except:
        return "There is an error with Frankfurter API"
    else:
        if resp.status_code == 200:
            return resp
        else:
            return "There is an error with Frankfurter API"