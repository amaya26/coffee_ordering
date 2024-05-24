flavours=["glazed","cinnamon","peanut butter",
          "chocolate","jam","custard","caramel"]
extras = ["Sprinkles","Chocolate sauce", "Crushed peanuts","Chocolate flakes"]

def show_menu():
    print("Shows menu. ")
    print()


while True:
    chosen_flavour = input("What flavour doughnut would you like? ").lower()
    if chosen_flavour in flavours:
        print("You chose {}.".format(chosen_flavour.capitalize()))

    elif chosen_flavour == "menu":
        show_menu()

    else:
        print("Oops! Looks like '{}' isn't in the menu. Please enter a valid doughnut flavour. ".format(chosen_flavour))