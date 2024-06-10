import pandas as pd
from tabulate import tabulate

# lists
flavours = ["Glazed","Cinnamon","Peanut Butter",
              "Chocolate","Jam","Custard","Caramel"]
toppings = ["Sprinkles","Chocolate sauce", "Crushed peanuts","Chocolate flakes"]
flavour_prices = [5, 5, 6, 6, 5, 6, 7]
topping_prices = [1, 2, 3, 3]

order = []

final_price = 0
while True:
    chosen_flavour = input("Flavour: ").capitalize()
    if chosen_flavour in flavours:
        print("You chose {}.".format(chosen_flavour))
        order.append(chosen_flavour) # add the flavour to the order list
        item_number = flavours.index(chosen_flavour) # find the position in the flavour list
        price = flavour_prices[item_number] # use same position in price list to get the price
        print("${}".format(price))
        final_price += price # add this to the total order price

    elif chosen_flavour == "Xxx": # once the exit code is entered, print the final order
        final_order = ", ".join(order)
        print("Your order: ")
        print(final_order)
        print("Total Cost: ${}".format(final_price))
        break

    else:
        print("Error".format(chosen_flavour))