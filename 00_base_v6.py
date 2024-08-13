import pandas as pd
from tabulate import tabulate
from datetime import date

# functions go here


# Runs the program to place an order
def run():
    final_order = []  # clear list from previous orders

    number_doughnuts = 0  # set the doughnut counter to 0
    print("\nWelcome to Dancing Doughnuts. You can order up to 10 doughnuts.")

    # Check the name input is not blank and hasn't been used for a previous order
    name = check_name("What name would you like to place the order under? (Press enter to confirm) ")
    # Check if user wants to view the menu
    want_menu = get_response("\nHi {}! Do you want to view the menu? ".format(name), ["yes", "no", "y", "n"],
                             "Please answer with yes or no. ")

    if want_menu == "yes" or want_menu == "y":
        show_menu()  # if input yes, run the menu function

    print("At any time type 'Menu' to view the menu, or 'xxx' to quit. ")

    while number_doughnuts < 10:  # repeat loop until limit of 10 reached
        print("\n***** Doughnut Number {} *****".format(number_doughnuts + 1))
        chosen_flavour = input("What flavour doughnut would you like? ").capitalize()  # capitalize to allow

        # comparison against flavour lists
        if chosen_flavour in flavours_list:  # if response is a valid flavour
            number_doughnuts += 1  # increase the doughnut counter
            print("{} doughnut added to order.".format(chosen_flavour))  # print confirmation of their order
            item_number = flavours_list.index(chosen_flavour)  # find the position in the flavour list
            item_price = flavour_prices[item_number]  # use that same position in price list to get the price
            order.append(chosen_flavour)  # add flavour to the order list
            order.append(item_price)  # add price to the order list
            # Check for a valid response
            want_toppings = get_response("\nWould you like to add any toppings? ", ["yes", "no", "y", "n"],
                                         "Please answer with yes or no. ").lower()

            # if the user wants to add toppings
            if want_toppings == "yes" or want_toppings == "y":
                print("You can order up to three toppings. Please enter 'xxx' when you are finished adding toppings. ")
                topping_number = 1  # reset the topping counter from previous orders
                total_price_toppings = 0 # reset the price from previous orders

                while topping_number < 4:  # repeat until max toppings reached
                    quit = False  # user did not enter exit code
                    chosen_topping = input("\nTopping number {}: ".format(topping_number)).capitalize()
                    if chosen_topping in toppings_list:  # if a valid topping is entered
                        print("You chose to add {}.".format(chosen_topping.lower()))
                        item_number = toppings_list.index(chosen_topping)  # find the position in the topping list
                        total_price_toppings += topping_prices[item_number]  # use same position in price list to get
                                                                             # the price of the topping and add to total
                                                                             # price
                        order.append(chosen_topping)  # add the topping to the order
                        topping_number += 1  # increase the topping counter

                    elif chosen_topping == "Xxx":  # if exit code is entered
                        quit = True  # the user quit before reaching the 3rd topping
                        while topping_number < 4: # add dashes to fill the empty topping spaces in the dataframe
                            order.append('-')  # add dashes in place of toppings in the dataframe list
                            topping_number += 1

                        doughnut_price = total_price_toppings + item_price  # find total price for single doughnut
                        order.append(doughnut_price)  # add price to the order list
                        final_order.append(order.copy())  # add info for this doughnut to the final order
                        order.clear()  # clear for next doughnut

                        break

                    elif chosen_topping == "Menu":  # if the user wants to view the menu
                        show_menu() # run the menu function

                    else:
                        print("Oops! Looks like '{}' isn't in the menu. "  # error for invalid responses
                              "Please enter a valid topping or enter 'xxx' to quit. ".format(chosen_topping))

                if not quit:  # if the user orders all 3 toppings without quitting
                    # need to add to the final order
                    doughnut_price = total_price_toppings + item_price  # get total price for doughnut
                    order.append(doughnut_price)  # add price to order list for this doughnut
                    final_order.append(order.copy())
                    # add the order (including flavour, toppings and price) to final
                    # order list
                    order.clear()  # clear for next order

            elif want_toppings == "no" or want_toppings == "n":  # if no toppings are ordered
                for x in range(0, 3):
                    order.append('-')  # add 3 placeholders to the dataframe
                order.append(item_price) # add the price for just the doughnut to the order list
                final_order.append(order.copy())
                order.clear()

        elif chosen_flavour == "Xxx":  # if the user quits when choosing a doughnut flavour
            if number_doughnuts == 0:  # check if this is their first doughnut
                # if it is first doughnut, print cancel message
                print("Your order has been cancelled.")
                again()  # ask if they want to make a new order
            else:
                break

        elif chosen_flavour == "Menu":
            show_menu()

        else:  # if flavour isn't in the menu then print error message
            print("Oops! Looks like '{}' isn't in the menu. "
                  "Please enter a valid doughnut flavour or enter 'xxx' to quit. ".format(chosen_flavour))

    # make a dataframe with the order
    # set column headings
    df = pd.DataFrame(final_order, columns=['Flavour', 'Price', 'Topping 1', 'Topping 2', 'Topping 3', 'Total Cost'])
    # start index from 1
    df.index = df.index + 1
    final_cost = df['Total Cost'].sum()  # calculate cost of order
    add_dollars = ['Price', 'Total Cost'] # format price columns with a dollar sign
    for var_item in add_dollars:
        df[var_item] = df[var_item].apply(currency)
    print()
    print(df)  # print the order dataframe
    print("\nYour total cost is: ${:.2f}".format(final_cost))  # print the final cost

    # ask for pickup or delivery and check for valid input
    delivery = get_response("\nThere is an extra charge of $4 for delivery. Would you like your order delivered? ",
                            ["yes", "no", "y", "n"], "Please answer with yes or no. ")
    if delivery == "yes" or delivery == "y":  # if choose delivery
        delivery_cost = 4  # add the surcharge
        final_cost += 4
        address = get_address()  # ask for an address and check it's valid
        print("Delivery cost: ${:.2f}".format(delivery_cost))
        # ask for phone number and check it's valid
        phone_number = num_check("What is your phone number? ", "Please enter a valid phone number. (Between 7 and 15"
                                                                " digits.) ")
    else:  # if not delivery
        print("Your order will be available to pick up in our shop.")

    payment_method = get_response("\nChoose a payment method(cash or credit): ", ["cash", "ca", "credit", "cr"],
                                  "Please answer with cash or credit. ")
    if payment_method == "credit" or payment_method == "cr":
        payment_surcharge = final_cost * 0.05  # add a credit surcharge to cost
        final_cost += payment_surcharge
        print("Card payment surcharge: ${:.2f}".format(payment_surcharge))

    print("Total Payment: ${:.2f}".format(final_cost))
    while True:
        # check if user wants to cancel their order
        confirm_cancel = get_response("\nPlease cancel or confirm your order? ", ["cancel", "confirm"],
                                       "Please answer with cancel or confirm. ").lower()
        if confirm_cancel == "cancel":
            print("Order cancelled. ")
            again()  # ask if they would like to place another order
        elif confirm_cancel == "confirm":
            print("Your order is being processed now.")
            name_list.append(name)  # add to the name list to ensure each order is under a different name
            break

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

    if delivery == "yes":  # add delivery info to the file
        extra_delivery = "Delivery Fee: ${:.2f}".format(delivery_cost)
        printed_address = "Delivery Address: {}".format(address)
        printed_phone_number = "Phone number: {}".format(phone_number)
        to_write.append(extra_delivery)
        to_write.append(printed_address)
        to_write.append(printed_phone_number)
    else:
        delivery_message = "Chose to pickup in store - No extra charge. "
        to_write.append(delivery_message)

    if payment_method == "credit":  # add payment info to the file
        extra_payment = "Payment Surcharge: ${:.2f}".format(payment_surcharge)
        to_write.append(extra_payment)
    else:
        payment_message = "Paid with cash - No extra charge. "
        to_write.append(payment_message)

    # add a heading and total to the file
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
        text_file.write("\n")  # add new lines between items

    # close file
    text_file.close()


# ask user if they want to order again
def again():
    while True:  # loop
        # use response checking function to check for valid input
        again = get_response("\nWould you like to place a new order? ", ["yes", "no", "n", "y"], "Please answer with yes"
                                                                                                "or no. ")
        if again == "yes" or again == "y":  # if they want to place a new order
            run()  # order again
        else:  # if finished ordering
            print("Thank you for choosing Dancing Doughnuts. ")
            exit()  # quit the program


# displays the menu in a dataframe
def show_menu():
    # using lists to create a menu dataframe
    flavour_menu = pd.DataFrame(list(zip(flavours_list, flavour_prices)),
                                columns=['Flavour', 'Price'])  # dataframe for flavours
    topping_menu = pd.DataFrame(list(zip(toppings_list, topping_prices)),
                                columns=['Topping', 'Price'])  # dataframe for toppings
    add_dollars = ['Price']  # format both price columns with dollar symbols
    for var_item in add_dollars:
        flavour_menu[var_item] = flavour_menu[var_item].apply(currency)  # apply the currency formatting funtion
        topping_menu[var_item] = topping_menu[var_item].apply(currency)

    print("\n***** Menu *****\n")
    print("***** Doughnut Flavours *****")
    print(tabulate(flavour_menu, showindex=False,  # remove index
                   headers=flavour_menu.columns))  # change the column headers
    print("\n***** Extras *****")
    print(tabulate(topping_menu, showindex=False,  # remove index
                   headers=topping_menu.columns))  # change column headers
    print()


# checks a response has a valid input
def get_response(question, valid_responses, error):
    while True:
        response = input(question).lower()  # convert to lowercase to allow comparison against list of valid responses

        if response in valid_responses:  # if input is in the list of valid responses
            return response  # return input

        else:  # if not a valid response
            print(error)


# checks that name is not blank and not a repeat of a past order name
def check_name(question):

    while True:
        response = input(question).capitalize()  # capitalize all names

        # if the response is blank, outputs an error
        if response == "":
            print("Sorry this can't be blank. Please try again")
        elif response in name_list:  # if response has already been used for an order
            print("You have already placed an order under that name. ")
        else:  # if valid response
            return response


# checks the address has both numbers and letters
def get_address():
    while True:
        address = input("What is your address? ")  # get user input
        number = any(map(str.isdigit, address))  # check input for digits
        string = any(map(str.isalpha, address))  # check input for letters
        if number is True and string is True:  # if input contains both numbers and letters
            return address

        else:
            print("Please enter a valid address. ")  # if response is invalid, print an error


# change numbers into a currency format
def currency(x):
    return "${:.2f}".format(x)


# checks that the phone number only contains numbers
def num_check(question, error):
    while True:
        response = input(question)  # get user input
        if response.isdigit() and 7 <= len(response) <= 15:  # if input is a number between 7 and 15
            return response
        else:  # if input not valid
            print(error)  # print an error message


# lists
flavours_list = ["Glazed", "Cinnamon", "Peanut Butter",
            "Chocolate", "Jam", "Custard", "Caramel"]
toppings_list = ["Sprinkles", "Chocolate sauce", "Crushed peanuts", "Chocolate flakes", "Pink icing"]
flavour_prices = [1, 5, 3, 6, 3, 4, 7]
topping_prices = [1, 2, 3, 2, 3]
order = []
final_order = []
name_list = []

# Run the program to place an order
run()

# once order is complete, ask user if they want to order again
again()
