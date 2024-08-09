
import pandas as pd
from tabulate import tabulate

# lists
flavours = ["Glazed","Cinnamon","Peanut Butter",
              "Chocolate","Jam","Custard","Caramel"]
toppings = ["Sprinkles","Chocolate sauce", "Crushed peanuts","Chocolate flakes"]
flavour_prices = [1, 5, 3, 6, 3, 4, 7]
topping_prices = [1, 5, 3, 6]
order = []

# functions go here

# prints the menu
def show_menu():
    # using lists to create menu dataframe
    flavour_menu = pd.DataFrame(list(zip(flavours, flavour_prices)),
                        columns=['Flavour', 'Price']) # dataframe for flavours
    topping_menu = pd.DataFrame(list(zip(toppings, topping_prices)),
                                columns=['Topping', 'Price']) # dataframe for toppings

    print("***** Menu *****\n")
    print("***** Doughnut Flavours *****")
    print(tabulate(flavour_menu, showindex=False, # remove index
                   headers=flavour_menu.columns))
    print("\n***** Extras *****")
    print(tabulate(topping_menu, showindex=False,
                   headers=topping_menu.columns)) # change the column headers
    print()


# checks responses for a yes or no question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no")


# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        # if the response is blank, outputs an error
        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


# main routine goes here
final_price = 0

# get user name
name = not_blank("What is your name? ").capitalize()

want_menu = yes_no("Do you want to view the menu? ")

if want_menu == "yes":
    show_menu()

while True:

    chosen_flavour = input("What flavour doughnut would you like? ").capitalize()

    if chosen_flavour in flavours:
        order.append(chosen_flavour)  # add the flavour to the order list
        item_number = flavours.index(chosen_flavour)  # find the position in the flavour list
        price = flavour_prices[item_number]  # use same position in price list to get the price
        print("Flavour: {} ${}".format(chosen_flavour, price))
        final_price += price  # add this to the total order price

        want_toppings = yes_no("Would you like to add any toppings? ").lower()
        if want_toppings == "yes":
            topping_number = 1 # reset the topping counter
            while topping_number < 4:
                chosen_topping = input("Topping number {}: ".format(topping_number)).capitalize()
                if chosen_topping in toppings:
                    print("You chose to add {}.".format(chosen_topping.lower()))
                    topping_number += 1 # increase the topping counter

                elif chosen_topping == "Menu":
                    show_menu()

                elif chosen_topping == "Xxx":
                    break

                else:
                    print("Oops! Looks like '{}' isn't in the menu. "
                          "Please enter a valid topping. ".format(chosen_topping))

    elif chosen_flavour == "Menu":
        show_menu()

    elif chosen_flavour == "Xxx":
        # if user quits, print their order
        final_order = ", ".join(order)
        print("Your order: ")
        print(final_order)
        print("Total Cost: ${}".format(final_price))
        break

    else:
        # error message
        print("Oops! Looks like '{}' isn't in the menu. "
              "Please enter a valid doughnut flavour. ".format(chosen_flavour))

