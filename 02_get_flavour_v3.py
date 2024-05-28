flavours=["glazed","cinnamon","peanut butter",
          "chocolate","jam","custard","caramel"]
extras = ["sprinkles","chocolate sauce", "crushed peanuts","chocolate flakes"]

def show_menu():
    print("***** Menu *****\n")
    print("***** Doughnut Flavours *****")
    print("{} $".format(flavours[0]))
    print("{} $".format(flavours[1]))
    print("{} $".format(flavours[2]))
    print("{} $".format(flavours[3]))
    print("{} $".format(flavours[4]))
    print("{} $".format(flavours[5]))
    print("{} $".format(flavours[6]))

    print("\n***** Extras *****")
    print("{} $".format(extras[0]))
    print("{} $".format(extras[1]))
    print("{} $".format(extras[2]))
    print("{} $".format(extras[3]))
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


topping_number = 1
while True:
    chosen_flavour = input("What flavour doughnut would you like? ").lower()
    if chosen_flavour in flavours:
        print("You chose {}.".format(chosen_flavour))

    elif chosen_flavour == "menu":
        show_menu()

    elif chosen_flavour == "xxx":
        break

    else:
        print("Oops! Looks like '{}' isn't in the menu. "
              "Please enter a valid doughnut flavour. ".format(chosen_flavour))

    want_toppings = yes_no("Would you like to add any toppings? ").lower()
    if want_toppings == "yes":
        while True:
            chosen_topping = input("Topping number {}: ".format(topping_number))
            if chosen_topping in extras:
                print("You chose {}.".format(chosen_topping.capitalize()))
                topping_number += 1

            elif chosen_topping == "menu":
                show_menu()

            elif chosen_topping == "xxx":
                break

            else:
                print("Oops! Looks like '{}' isn't in the menu. "
                      "Please enter a valid topping. ".format(chosen_topping))