# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered


# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
#recreating the order list and then appending it overides the previous order_list don't
order_list = []
# trying to create a function to keep ordering
place_order = True
while place_order:

    print("From which menu would you like to order")

    i = 1

    menu_items = {}

    for key in menu.keys():
        print(f"{i}: {key}")

        menu_items[i] = key

        i += 1

    menu_category = input ("Type menu number: ")

    if int(menu_category.isdigit()):
        
        if int(menu_category) in menu_items.keys():

            menu_category_name = menu_items[int(menu_category)]

            print(f"You selected {menu_category_name}")

            print(f"What {menu_category_name} would you like to order?")

            i = 1
            menu_items = {}          
            print("Item # | Item name                | Price")           
            print("-------|--------------------------|-------")           
            for key, value in menu[menu_category_name].items():
                    # Check if the menu item is a dictionary to handle differently               
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1

                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
    
        
            while True:
                
                    menu_item_number = input ("Please type the number of the menu item you would like. : ")
                
                    if menu_item_number.isdigit() and int(menu_item_number) in menu_items.keys():
                    
                        #if int(menu_item_number) in menu_items.keys():

                        menu_item_number = menu_items[int(menu_item_number)]
                        
                        item_name = menu_item_number["Item name"]
                        item_price = menu_item_number ["Price"]
                        item_price = float(item_price)
                        

                        print(f"You've selected {item_name}")
                        while True:
                            Quantity = input (f"How many {item_name}s would you like?:  ")

                            if Quantity.isdigit():
                                Quantity = int(Quantity)
                                break

                            else:
                                print("Error, Please enter a valid number")


                        order_list.append ({
                            "Item Name" : item_name,
                            "Price" : item_price,
                            "Quantitiy" : Quantity
                        })
                        break
                    else:
                        print( "Error! Your selection is invalid.")
                        
        else:
                # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
                # Tell the customer they didn't select a number
        print(f"Error! {menu_category} is not a valid number a number.")
                
    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

            # 5. Check the customer's input
        if keep_ordering.lower() == "y" :
            #print("\nWhat items would you like to add?\n")
            break

        elif keep_ordering.lower() == "n" :
            print('Thank you for your order!')
            place_order= False
            break

        else :
            
            print ("Sorry, Please enter 'Y or N'.")

#i = 1
total = 0
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------") 


for order in order_list:
    item = order["Item Name"]
    price = order["Price"]
    quan = order ["Quantitiy"]

    num_item_spaces = 25 - len(item)
    item_spaces = " " * num_item_spaces
    Item_spaces =  5 - len(str(price))
    more_spaces = " " * Item_spaces
    print(f"{item}{item_spaces} | ${price}{more_spaces} | {quan}")

    total += price * quan
total ="{:.2f}".format(total)
print(f"\nTotal: ${total}")
