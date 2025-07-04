''' Here we import catalogue, product info from "add" module'''
from add import catalogue, product_info

'''  A blanket function buying() was created to enclose other functions in this module.
        This is so that it can easily be called in other prompt.py module '''


def buying():

    # ''' validate_coin() module ensures that all possible user input errors are prevented.'''
    def validate_coin():
        while True:
            try:
                insert_coin = int(input("PLEASE INSERT A COIN AND PRESS ENTER KEY TO CONTINUE:\n"))
                show = f"You have entered {insert_coin} pence.\nThese are the products you can purchase:\n"

            except ValueError:
                print("That is not a coin.")
                continue

            print(show)

            # ''' what_user_see() function limits product displayed based on the amount entered in to the machine '''
            def what_user_see():

                if insert_coin >= 50:
                    print(catalogue)

                elif 49 >= insert_coin >= 20:
                    print(catalogue[catalogue["PRICE"] < 50])

                elif 19 >= insert_coin >= 10:
                    print(catalogue[catalogue["PRICE"] < 20])

                elif 9 >= insert_coin >= 5:
                    print(catalogue[catalogue['PRICE'] < 10])

                elif 5 > insert_coin != 0:
                    print(catalogue[catalogue['PRICE'] < 5])

                else:
                    print(f" no item to purchase")

            what_user_see()
            return insert_coin

    ##  variable 'coin' is used to store the value of coin earlier validated .
    ##  This allows it to be passed as parameter later in the code'''
    coin = validate_coin()




    def validate_code_input():          # ''' validate_code_input() function is used to ensure user input correct product code.'''
        while True:
            product_code = str(input("PLEASE ENTER THE CODE OF THE ITEM YOU WANT AND PRESS ENTER KEY: \n").upper())

            if product_code.isnumeric():
                print(f"{product_code} is a number not an item code.")
                continue

            if product_code not in product_info["ITEM_CODE"]:
                print("This item is not available in this machine.")
                continue
            else:
                return product_code

    code = validate_code_input()   # The product code earlier validated is stored in variable 'code' so it can also be passed as a parameter

#  This function

    def remaining_coin(coin, price_of_item):
        coin = coin - price_of_item
        return coin



        # ''' This function  serves as a prompt for users if they still wan to continue purchase'''

    def validate_yes_no():
        while True:
            answer = str(input(f"Will you like another item? Y or N?\n")).upper()

            if answer == "Y":
                return answer
            elif answer == "N":
                return answer
            else:
                continue

        # '''This function does the following:'''

    def purchase(code, coin):

        ''' Since we are using pandas dataframe to display product in tabular form,
         we also use it to map product code to item and priceRetrieves the name and price of item and display with print function '''

        price_of_item = catalogue.loc[catalogue['ITEM_CODE'] == code, 'PRICE'].item()
        name_of_item = catalogue.loc[catalogue['ITEM_CODE'] == code, 'ITEMS'].item()
        print(f'You have chosen {name_of_item}. That will be {price_of_item} pence')

        if coin < price_of_item:
            print("Insufficient coin. Choose another product or quit\n")

            # If a user selects an item with a higher price than coin inserted, the following lines allows them the option of quiting or continue their purchase.
            tester = input("Do you want to continue? \nEnter Yes or No:  ").lower()
            if tester == 'yes':
                purchase(validate_code_input(), coin)
            else:
                print("Thanks for your time")

        # The following lines terminates the code when a user has purchased an item that is equivalent to the item bought.
        elif coin == price_of_item:
            print("Thank you for your patronage\n")
            print(f"Your have no change")

        # If user purchase is less than the coin they input
        elif coin > price_of_item:
            change = remaining_coin(coin, price_of_item)
            print(f"Your change is {change} pence")

            # if user still has change, they have the option to purchase another item within their coin range
            if change >= 5:
                new_order_2 = validate_yes_no()

                if new_order_2 == "Y":
                    val = validate_code_input()
                    coin = change
                    purchase(val, coin)

                elif new_order_2 == "N":
                    print(f"Thank you for your purchase.\nYour change is {change} pence.")
            else:
                print(f"you can no longer purchase")

    purchase(code, coin)
