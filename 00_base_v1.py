# lists
extras = ["Sprinkles","Chocolate sauce", "Crushed peanuts",
          "Chocolate flakes"]
flavours=["glazed","cinnamon","peanut butter",
          "chocolate","jam","custard","caramel"]

# functions go here

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

# main routine goes here


want_instructions = yes_no("Do you want to view the menu? ")

if want_instructions == "yes":
    show_menu()

while True:
    chosen_flavour = input("What flavour doughnut would you like? ").lower()
    if chosen_flavour in flavours:
        print("You chose {}.".format(chosen_flavour.capitalize()))

    elif chosen_flavour == "menu":
        show_menu()

    else:
        print("Oops! Looks like '{}' isn't in the menu. Please enter a valid doughnut flavour. ".format(chosen_flavour))

