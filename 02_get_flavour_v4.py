flavours = ["Glazed","Cinnamon","Peanut Butter",
              "Chocolate","Jam","Custard","Caramel"]
toppings = ["Sprinkles","Chocolate sauce", "Crushed peanuts","Chocolate flakes"]
def show_menu():
    print("shows menu")


def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no")


topping_number = 1
while True:
    chosen_flavour = input("What flavour doughnut would you like? ").capitalize()
    if chosen_flavour in flavours:
        print("Flavour: {}".format(chosen_flavour))

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
        break

    else:
        print("Oops! Looks like '{}' isn't in the menu. "
              "Please enter a valid doughnut flavour. ".format(chosen_flavour))
