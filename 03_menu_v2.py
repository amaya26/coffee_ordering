flavours = ["Glazed","Cinnamon","Peanut Butter",
              "Chocolate","Jam","Custard","Caramel"]
extras = ["Sprinkles","Chocolate sauce", "Crushed peanuts","Chocolate flakes"]


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


show_menu()