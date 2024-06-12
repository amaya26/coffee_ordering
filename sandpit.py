flavours = ["Glazed","Cinnamon","Peanut Butter",
              "Chocolate","Jam","Custard","Caramel"]
toppings = ["Sprinkles","Chocolate sauce", "Crushed peanuts","Chocolate flakes"]
flavour_prices = [5, 5, 6, 6, 5, 6, 7]
topping_prices = [1, 2, 3, 3]

order = []
final_order = []
topping_number = 0


def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no")

while True:
    chosen_flavour = input("Flavour: ").capitalize()
    if chosen_flavour in flavours:
        print("You chose {}.".format(chosen_flavour))
        item_number = flavours.index(chosen_flavour)  # find the position in the flavour list
        price = flavour_prices[item_number]  # use same position in price list to get the price
        order.append(chosen_flavour)
        order.append(price)
        want_toppings = yes_no("Would you like to add any toppings? ").lower()
        if want_toppings == "yes":
            topping_number = 1  # reset the topping counter
            while topping_number < 4:
                chosen_topping = input("Topping number {}: ".format(topping_number)).capitalize()
                if chosen_topping in toppings:
                    print("You chose to add {}.".format(chosen_topping.lower()))
                    item_number = toppings.index(chosen_topping)  # find the position in the flavour list
                    price_topping = topping_prices[item_number]  # use same position in price list to get the price
                    order.append(chosen_topping)
                    order.append(price_topping)
                    topping_number += 1  # increase the topping counter

                elif chosen_topping == "Xxx":
                    final_order.append(order.copy())
                    order.clear()

                    break

                else:
                    print("Oops! Looks like '{}' isn't in the menu. "
                          "Please enter a valid topping. ".format(chosen_topping))

    elif chosen_flavour == "Xxx": # once the exit code is entered, print the final order
        break

    else:
        print("Error".format(chosen_flavour))

print(final_order)