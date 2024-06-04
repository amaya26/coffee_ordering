

flavours = ["Glazed","Cinnamon","Peanut Butter",
              "Chocolate","Jam","Custard","Caramel"]
flavour_prices = [1, 5, 3, 6, 3, 4, 7]
order = []

final_price = 0
while True:
    chosen_flavour = input("Flavour: ").capitalize()
    if chosen_flavour in flavours:
        print("You chose {}.".format(chosen_flavour))
        order.append(chosen_flavour) # add the flavour to the order list
        item_number = flavours.index(chosen_flavour)
        price = flavour_prices[item_number]
        print("${}".format(price))
        final_price += price

    elif chosen_flavour == "Xxx":
        final_order = ", ".join(order)
        print("Your order: ")
        print(final_order)
        print("Total Cost: ${}".format(final_price))
        break

    else:
        print("Error".format(chosen_flavour))