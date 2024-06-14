import pandas as pd
from tabulate import tabulate

# functions go here

def show_menu():
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
    print()


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


def get_address():
    while True:
        address = input("What is your address? ")
        number = any(map(str.isdigit, address))
        string = any(map(str.isalpha, address))
        if number == True and string == True:
            return address

        else:
            print("Please enter a valid address. ")


def currency(x):
    return "${:.2f}".format(x)


# lists
flavours = ["Glazed","Cinnamon","Peanut Butter",
              "Chocolate","Jam","Custard","Caramel"]
toppings = ["Sprinkles","Chocolate sauce", "Crushed peanuts","Chocolate flakes"]
flavour_prices = [1, 5, 3, 6, 3, 4, 7]
topping_prices = [1, 5, 3, 6]
order = []
final_order = []


# main routine goes here
number_doughnuts = 0

name = not_blank("What is your name? ").capitalize()
want_menu = yes_no("Hi {}! Do you want to view the menu? ".format(name))

if want_menu == "yes":
    show_menu()

while number_doughnuts < 10:
    chosen_flavour = input("What flavour doughnut would you like? ").capitalize()
    if chosen_flavour in flavours:
        print("You chose {}.".format(chosen_flavour))
        item_number = flavours.index(chosen_flavour)  # find the position in the flavour list
        price = flavour_prices[item_number]  # use same position in price list to get the price
        order.append(chosen_flavour)
        order.append(price)
        want_toppings = yes_no("Would you like to add any toppings? ").lower()

        if want_toppings == "yes":
            topping_number = 1  # reset the topping counter
            price_topping = 0

            while topping_number < 4:
                chosen_topping = input("Topping number {}: ".format(topping_number)).capitalize()
                if chosen_topping in toppings:
                    print("You chose to add {}.".format(chosen_topping.lower()))
                    item_number = toppings.index(chosen_topping)  # find the position in the flavour list
                    price_topping += topping_prices[item_number]  # use same position in price list to get the price
                    order.append(chosen_topping)
                    topping_number += 1  # increase the topping counter

                elif chosen_topping == "Xxx":
                    while topping_number < 4:
                        order.append('-')
                        topping_number += 1

                    dougnut_price = price_topping + price
                    order.append(dougnut_price)
                    final_order.append(order.copy())
                    order.clear()

                    break

                elif chosen_topping == "Menu":
                    show_menu()

                else:
                    print("Oops! Looks like '{}' isn't in the menu. "
                          "Please enter a valid topping. ".format(chosen_topping))

                dougnut_price = price_topping + price
                order.append(dougnut_price)
                final_order.append(order.copy())
                order.clear()

        else:
            order.append('-')
            order.append('-')
            order.append('-')
            order.append(price)
            final_order.append(order.copy())
            order.clear()

    elif chosen_flavour == "Xxx":
        break

    elif chosen_flavour == "Menu":
        show_menu()

    else:
        print("Oops! Looks like '{}' isn't in the menu. "
              "Please enter a valid doughnut flavour. ".format(chosen_flavour))

get_address()

df = pd.DataFrame(final_order, columns=['Flavour', 'Price', 'Topping 1', 'Topping 2', 'Topping 3', 'Total Cost'])
df.index = df.index + 1
add_dollars = ['Price', 'Total Cost']
for var_item in add_dollars:
    df[var_item] = df[var_item].apply(currency)
print(df)
