import pandas as pd
product_info = {
    "ITEMS": ["Slim Bar", "Far Bar", "Mar Bar", "Twin Bar"],
    "PRICE": [5, 10, 20, 50],
    "ITEM_CODE": ["SB", "FB", "MB", "TB"]
    }

regex_name = "^[a-z A-Z]*$"
password = 12345
catalogue = pd.DataFrame(product_info)