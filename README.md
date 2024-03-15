# <Currency Converter>

## Author
Name: Prinston Mascarenhas
Student ID: 24587331

## Description
<What your application does>
The application takes in three inputs : <Date><Currency1><Currency2>
It then converts one currency to another and provides us the conversion rate as well as the inversion rate. It also validates data inputs and returns an appropriate response.
<Some of the challenges you faced>
The unittest cases were a challenge to me as I've never worked on Python before. But nevertheless, I loved working on this assignment.
<Some of the features you hope to implement in the future>
Implementing a nice UI would seem like the next feature I would like to work on.

## How to Setup
<Provide a step-by-step description of how to get the development environment set and running.>
Step 1: install virtual env using pip
        "pip install virtualenv"

Step 2: Create a directory
        mkdir currencyConverter
        
Step 3: To use the virtual env , use the following command :
        python<version> -m venv <virtual-environment-name>
        
Step 4: activate virtual environment
        source 
<Which Python version you used>
Python 3.9.0
<Which packages and version you used>
1)requests  2.28.1
2)urllib3   1.26.11

## How to Run the Program
python main.py <Date><Currency1><Currency2>

example : python main.py 2022-01-01 GBP AUD 

## Project Structure

main.py: main program used for running your business logics

checks.py: python script that will contain the code for checking inputted arguments and date validity

api.py: python script that will contain the code for making API calls

frankfurter.py: python script that will contain the class used for calling relevant Frankfurter endpoints

currency.py: python script that will contain the class used for extracting currency conversion rate and calculating the inverse rate

test_checks.py: python script for testing code from checks.py

test_frankfurter.py: python script for testing code from frankfurter.py

test_api.py: python script for testing code from api.py

test_currency.py: python script for testing code from currency.py

README.md: a markdown file containing details (full name, student id), a description of this project, listing of all Python functions and classes and instructions for running the code 

## Citations
<Mention authors and provide links code you source externally>

None