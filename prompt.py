''' The following variables were declared in a separate module "variables.py" for ease of access to every other module in the program:
Product_info: a dictionary that contains the given products, there code and price.
regex_name: this was used to validate user input for product name.
       This is to allow product names with multiple words separated by whitespace to be entered in to the dictionary.
password: this variable stores the administrative password for the manager.
catalogue: this variable stores the dictionary "product_info" in a table with the use of pandas library.
         pandas library was employed as a form as aesthetic for the display in the terminal.'''
from add import *
from buy import *

''' The function procedure() serves as the home screen that allows a user choose either to
 purchase product or add products depending on the privileges they have.'''


def procedure():
    process = str(input('Enter "A" to Add Products or "P" to Purchase or "Q" to Quit: ')).upper()
    if process == "A":
        adding_products()

    elif process == "P":
        buying()

    elif process == "Q":
        print("Thank You for Visiting")


procedure()
