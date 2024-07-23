import pandas as pd
from tabulate import tabulate
from datetime import date

# functions go here

# Runs the program to place an order
def run():
    final_order = [] # clear from previous orders

    number_doughnuts = 0 # set the counter to 0
    print("\nWelcome to *super cool business name*. You can order up to 10 doughnuts. At any time "
          "type 'Menu' to view the menu, or 'xxx' to quit. \n")
    name = check_name("What name would you like to place the order under? ")
    name_list.append(name) # add to the name list to ensure each order is under a different name
    want_menu = yes_no("\nHi {}! Do you want to view the menu? ".format(name))

    if want_menu == "yes":
        show_menu()

    while number_doughnuts < 10: # repeat until limit reached
        chosen_flavour = input("\nWhat flavour doughnut would you like? ").capitalize() # capitalize to allow
        # comparison against lists
        if chosen_flavour in flavours:
            number_doughnuts += 1
            print("{} doughnut added to order.".format(chosen_flavour))
            item_number = flavours.index(chosen_flavour)  # find the position in the flavour list
            price = flavour_prices[item_number]  # use same position in price list to get the price
            order.append(chosen_flavour)
            order.append(price)
            want_toppings = yes_no("\nWould you like to add any toppings? ").lower()

            if want_toppings == "yes":
                topping_number = 1  # reset the topping counter
                price_topping = 0

                while topping_number < 4: # repeat until max doughnuts reached
                    quit = False
                    chosen_topping = input("\nTopping number {}: ".format(topping_number)).capitalize()
                    if chosen_topping in toppings:
                        print("You chose to add {}.".format(chosen_topping.lower()))
                        item_number = toppings.index(chosen_topping)  # find the position in the flavour list
                        price_topping += topping_prices[item_number]  # use same position in price list to get the price
                        order.append(chosen_topping)
                        topping_number += 1  # increase the topping counter

                    elif chosen_topping == "Xxx": # if exit code is entered
                        quit = True
                        while topping_number < 4:
                            order.append('-') # add dashes in place of toppings in the dataframe list
                            topping_number += 1

                        dougnut_price = price_topping + price # work out total price
                        order.append(dougnut_price) # add price to the order list
                        final_order.append(order.copy()) # add info for this doughnut to the final order
                        order.clear() # clear for next doughnut

                        break

                    elif chosen_topping == "Menu":
                        show_menu()

                    else:
                        print("Oops! Looks like '{}' isn't in the menu. " # error for invalid responses
                              "Please enter a valid topping. ".format(chosen_topping))

                if quit == False: # if the user orders all 3 toppings without quitting
                    dougnut_price = price_topping + price
                    order.append(dougnut_price)
                    final_order.append(order.copy())
                    order.clear()

            elif want_toppings == "no":
                for x in range (0,3):
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

    df = pd.DataFrame(final_order, columns=['Flavour', 'Price', 'Topping 1', 'Topping 2', 'Topping 3', 'Total Cost'])
    df.index = df.index + 1
    final_cost = df['Total Cost'].sum()
    add_dollars = ['Price', 'Total Cost']
    for var_item in add_dollars:
        df[var_item] = df[var_item].apply(currency)
    print()
    print(df)
    print("\nYour total cost is: ${:.2f}".format(final_cost))

    delivery = yes_no("\nWould you like your order delivered? ")
    if delivery == "yes":
        delivery_cost = 4
        final_cost += 4
        address = get_address()
        print("Delivery cost: ${:.2f}".format(delivery_cost))
        phone_number = num_check("What is your phone number? ", "Please enter a number.")
    else:
        print("Your order will be available to pick up in our shop.")

    payment_method = cash_credit("\nChoose a payment method(cash or credit): ")
    if payment_method == "credit":
        payment_surcharge = final_cost * 0.05
        final_cost += payment_surcharge
        print("Card payment surcharge: ${:.2f}".format(payment_surcharge))

    print("Total Payment: ${:.2f}".format(final_cost))
    while True:
        confirm_cancel = input("\nPlease cancel or confirm your order? ").lower()
        if confirm_cancel == "cancel":
            print("Order cancelled. ")
            exit()
        elif confirm_cancel == "confirm":
            print("Your order is being processed now.")
            break
        else:
            print("Please type either cancel or confirm. ")

    # **** get current date for heading and filename ****
    # get today's date
    today = date.today()

    # get day, month and year as individual strings
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")

    heading = "\n---- {}'s Doughnut Order ({}/{}/{}) ---- \n".format(name, day, month, year)
    filename = "{}'s Order_{}_{}_{}".format(name, day, month, year)

    # change frame to a string so that we can export it to file
    order_string = pd.DataFrame.to_string(df)

    extra_costs_heading = "\n------- Extra Costs ------- "

    to_write = [heading, order_string, extra_costs_heading]

    if delivery == "yes":
        extra_delivery = "Delivery Fee: ${:.2f}".format(delivery_cost)
        printed_address = "Delivery Address: {}".format(address)
        printed_phone_number = "Phone number: {}".format(phone_number)  # come back to thisssss
        to_write.append(extra_delivery)
        to_write.append(printed_address)
        to_write.append(printed_phone_number)
    else:
        delivery_message = "Chose to pickup in store - No extra charge. "
        to_write.append(delivery_message)

    if payment_method == "credit":
        extra_payment = "Payment Surcharge: ${:.2f}".format(payment_surcharge)
        to_write.append(extra_payment)
    else:
        payment_message = "Paid with cash - No extra charge. "
        to_write.append(payment_message)

    total_heading = "\n------ Order Total ------"
    total_text = "Total Cost: ${:.2f}".format(final_cost)
    to_write.append(total_heading)
    to_write.append(total_text)

    # write output to file
    # create file to hold data (add .txt extension)
    write_to = "{}.txt".format(filename)
    text_file = open(write_to, "w+")

    for item in to_write:
        text_file.write(item)
        text_file.write("\n")

    # close file
    text_file.close()


# displays the menu in a dataframe
def show_menu():
    flavour_menu = pd.DataFrame(list(zip(flavours, flavour_prices)),
                        columns=['Flavour', 'Price'])
    topping_menu = pd.DataFrame(list(zip(toppings, topping_prices)),
                                columns=['Topping', 'Price'])
    add_dollars = ['Price']
    for var_item in add_dollars:
        flavour_menu[var_item] = flavour_menu[var_item].apply(currency)
        topping_menu[var_item] = topping_menu[var_item].apply(currency)

    print("\n***** Menu *****\n")
    print("***** Doughnut Flavours *****")
    print(tabulate(flavour_menu, showindex=False,
                   headers=flavour_menu.columns))
    print("\n***** Extras *****")
    print(tabulate(topping_menu, showindex=False,
                   headers=topping_menu.columns))
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


# checks that name is not blank and not a repeat of a past order name
def check_name(question):

    while True:
        response = input(question).capitalize()

        # if the response is blank, outputs an error
        if response == "":
            print("Sorry this can't be blank. Please try again")
        elif response in name_list:
            print("You have already placed an order under that name. ")
        else:
            return response


# checks the address has both numbers and letters
def get_address():
    while True:
        address = input("What is your address? ")
        number = any(map(str.isdigit, address))
        string = any(map(str.isalpha, address))
        if number == True and string == True:
            return address

        else:
            print("Please enter a valid address. ")


# change numbers into a currency format
def currency(x):
    return "${:.2f}".format(x)


# checks that the phone number only contains numbers
def num_check(question, error):
    valid = False
    while not valid:

        response = input(question)
        if response.isdigit():
            return response
        else:
            print(error)


# Check user response to the cash or credit question
def cash_credit(question):
    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            return "cash"

        elif response == "credit" or response == "cr":
            return "credit"

        else:
            print("Please enter a valid payment method")


# lists
flavours = ["Glazed", "Cinnamon", "Peanut Butter",
            "Chocolate", "Jam", "Custard", "Caramel"]
toppings = ["Sprinkles", "Chocolate sauce", "Crushed peanuts", "Chocolate flakes","Pink icing"]
flavour_prices = [1, 5, 3, 6, 3, 4, 7]
topping_prices = [1, 2, 3, 2, 3]
order = []
final_order = []
name_list = []

# Run the program to place one order
run()

# once order is complete, ask user if they want to order again
while True:
    again = yes_no("\nWould you like to place another order?")
    if again == "yes":
        run() # order again
    else:
        print("Thank you for ordering from *super cool business name*.")
        exit() # quit the program


