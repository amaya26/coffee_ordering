import pandas as pd
from tabulate import tabulate

# lists
flavours = ["Glazed","Cinnamon","Peanut Butter",
              "Chocolate","Jam","Custard","Caramel"]
toppings = ["Sprinkles","Chocolate sauce", "Crushed peanuts","Chocolate flakes"]
flavour_prices = [1, 5, 3, 6, 3, 4, 7]
topping_prices = [1, 5, 3, 6]

# functions
def show_menu(): # combine the lists into a menu
    flavour_menu = pd.DataFrame(list(zip(flavours, flavour_prices)),
                        columns=['Flavour', 'Price'])
    topping_menu = pd.DataFrame(list(zip(toppings, topping_prices)),
                                columns=['Topping', 'Price'])

    print("***** Menu *****\n")
    print("***** Doughnut Flavours *****")
    print(tabulate(flavour_menu, showindex=False,
                   headers=flavour_menu.columns))
    print("\n***** Extras *****")
    print(tabulate(topping_menu, showindex=False,
                   headers=topping_menu.columns))

# main routine
show_menu()
