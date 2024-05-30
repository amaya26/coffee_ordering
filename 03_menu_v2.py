flavours = ["Glazed","Cinnamon","Peanut Butter",
              "Chocolate","Jam","Custard","Caramel"]
extras = ["Sprinkles","Chocolate sauce", "Crushed peanuts","Chocolate flakes"]


def show_menu():
    print("***** Menu *****\n")
    print("***** Doughnut Flavours *****")
    for item in flavours:
        print(item)

    print("\n***** Extras *****")
    print("{} $".format(extras[0]))
    print("{} $".format(extras[1]))
    print("{} $".format(extras[2]))
    print("{} $".format(extras[3]))
    print()


show_menu()