''' This line was used to call ALL the declared variables from the variable.py module '''
from variables import *

'''  The function adding_products is only accessible when a user has administrative privileges.
The user is prompted to state how many products they would like to insert and using the 'for loop',
   the user keeps getting prompts until the iteration is over '''


def adding_products():
    while True:
        try:
            correct_password = int(input("Enter Admin Password: "))

            if correct_password != password:
                print(f"Enter Correct Password.")
                continue
        except ValueError:
            print("Enter Numbers Only")
            continue

        else:
            number_of_product = input("How Many Products Will You Like To Add?: ")
            if not number_of_product.isdigit():
                print("Invalid Input")
                continue
            else:
                for num in range(int(number_of_product)):
                    while True:
                        product_code = str(input("Enter Product Code(use the first alphabet of each word): ")).upper()

                        if product_code not in product_info["ITEM_CODE"] and product_code.isalpha():
                            product_info["ITEM_CODE"].append(product_code)
                            break
                        else:
                            print("This Code Exists! Enter Unique Code")

                    while True:
                        product_name = str(input(f"Enter Product Name:  ")).title()
                        if not regex_name:          # regex was implemented to allow products with multiple word name be added.
                            print("Enter Word(s)")

                        else:
                            product_info["ITEMS"].append(product_name)
                            break

                    while True:
                        product_price = input("Enter Product Price: ")
                        if product_price.isdigit():
                            product_info["PRICE"].append(product_price)
                            break
                        else:
                            print("Enter Numbers")
                catalogue = pd.DataFrame(product_info)
                print(catalogue)
                return catalogue


'''
To improve on this, product_info can be stored in a CSV file.
A CSV file will serve as a database so it can retain user input that can be accessed at anytime.
A sample code is to store the product_info dictionary to csv file is  :
         with open('product_info.csv', 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(product_info.keys())
            writer.writerows(zip(*product_info.values()))
 '''