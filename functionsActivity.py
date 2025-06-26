menu = {'Pizza': 2.99, 
        'Burger': 3.99,
        'Hot dog': 1.99, 
        'Cheese': 0.59,
        'Ice cream': 1.49,
        'Churro': 0.79, 
        'Soda': 0.89}

def total_price(item1, item2):
   total = menu[item1] + menu[item2]
   return f"The sum of {item1} and {item2} is {total}"


def  price_difference(item1, item2):
    difference = menu[item1] - menu[item2]
    return f"The difference between {item1} and {item2} is {difference}"

def inflation(item):
    new_price = menu[item] * 1.05
    menu[item] = new_price
    return menu
    return f"The new price of {item} after inflation is {new_price}"

def deflation (item):
    new_price = menu[item] / 1.05
    menu[item] = new_price
    return menu
    return f"The new price of {item} after deflation is {new_price}"

def add_item(item, price):
    menu[item] = price
    return f"{item} has been added to the menu with a price of {price}"