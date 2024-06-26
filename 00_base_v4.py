import pandas as pd
from tabulate import tabulate
from datetime import date

# functions go here

def show_menu():
    flavour_menu = pd.DataFrame(list(zip(flavours, flavour_prices)),
                        columns=['Flavour', 'Price'])
    topping_menu = pd.DataFrame(list(zip(toppings, topping_prices)),
                                columns=['Topping', 'Price'])

    print("***** Menu *****\n")
    print("***** Doughnut Flavours *****")
    print(tabulate(flavour_menu, showindex=False,
                   headers=flavour_menu.columns))
    print("\n***** Extras *****")
    print(tabulate(topping_menu, showindex=False,
                   headers=topping_menu.columns))
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


# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        # if the response is blank, outputs an error
        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


def get_address():
    while True:
        address = input("What is your address? ")
        number = any(map(str.isdigit, address))
        string = any(map(str.isalpha, address))
        if number == True and string == True:
            return address

        else:
            print("Please enter a valid address. ")


def currency(x):
    return "${:.2f}".format(x)


def num_check(question, error):
    valid = False
    while not valid:

        response = input(question)
        if response.isdigit():
            return response
        else:
            print(error)


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
flavours = ["Glazed","Cinnamon","Peanut Butter",
              "Chocolate","Jam","Custard","Caramel"]
toppings = ["Sprinkles","Chocolate sauce", "Crushed peanuts","Chocolate flakes"]
flavour_prices = [1, 5, 3, 6, 3, 4, 7]
topping_prices = [1, 5, 3, 6]
order = []
final_order = []


# main routine goes here
number_doughnuts = 0

name = not_blank("What is your name? ").capitalize()
want_menu = yes_no("Hi {}! Do you want to view the menu? ".format(name))

if want_menu == "yes":
    show_menu()

while number_doughnuts < 10:
    chosen_flavour = input("What flavour doughnut would you like? ").capitalize()
    if chosen_flavour in flavours:
        number_doughnuts += 1
        print("You chose {}.".format(chosen_flavour))
        item_number = flavours.index(chosen_flavour)  # find the position in the flavour list
        price = flavour_prices[item_number]  # use same position in price list to get the price
        order.append(chosen_flavour)
        order.append(price)
        want_toppings = yes_no("Would you like to add any toppings? ").lower()

        if want_toppings == "yes":
            topping_number = 1  # reset the topping counter
            price_topping = 0

            while topping_number < 4:
                quit = False
                chosen_topping = input("Topping number {}: ".format(topping_number)).capitalize()
                if chosen_topping in toppings:
                    print("You chose to add {}.".format(chosen_topping.lower()))
                    item_number = toppings.index(chosen_topping)  # find the position in the flavour list
                    price_topping += topping_prices[item_number]  # use same position in price list to get the price
                    order.append(chosen_topping)
                    topping_number += 1  # increase the topping counter

                elif chosen_topping == "Xxx":
                    quit = True
                    while topping_number < 4:
                        order.append('-')
                        topping_number += 1

                    dougnut_price = price_topping + price
                    order.append(dougnut_price)
                    final_order.append(order.copy())
                    order.clear()

                    break

                elif chosen_topping == "Menu":
                    show_menu()

                else:
                    print("Oops! Looks like '{}' isn't in the menu. "
                          "Please enter a valid topping. ".format(chosen_topping))

            if quit == False:
                dougnut_price = price_topping + price
                order.append(dougnut_price)
                final_order.append(order.copy())
                order.clear()

        elif want_toppings == "no":
            order.append('-')
            order.append('-')
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
print(df)
print("Your total cost is: ${:.2f}".format(final_cost))
while True:
    confirm_cancel = input("Please cancel or confirm your order? ").lower()
    if confirm_cancel == "cancel":
        print("Order cancelled")
        exit()
    elif confirm_cancel == "confirm":
        print("You have confirmed your order.")
        break
    else:
        print("Please type either cancel or confirm. ")

delivery = yes_no("Would you like your order delivered? ")
if delivery == "yes":
    delivery_cost = 4
    final_cost += 4
    address = get_address()
    print("Delivery cost: ${:.2f}".format(delivery_cost))
    phone_number = num_check("What is your phone number? ", "Please enter a number.")
else:
    print("Your order will be available to pick up in our shop.")

payment_method = cash_credit("Choose a payment method(cash or credit): ")
if payment_method == "credit":
    payment_surcharge = final_cost * 0.05
    final_cost += payment_surcharge
    print("Card payment surcharge: ${:.2f}".format(payment_surcharge))


print("Total Payment: ${:.2f}".format(final_cost))
print("Your order is being processed now.")

# **** get current date for heading and filename ****
# get today's date
today = date.today()

# get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "\n---- {}'s Doughnut Order ({}/{}/{}) ---- \n".format(name,day, month, year)
filename = "Order_{}_{}_{}".format(day, month, year)

# change frame to a string so that we can export it to file
order_string = pd.DataFrame.to_string(df)

extra_costs_heading = "\n------- Extra Costs ------- "

to_write = [heading, order_string, extra_costs_heading]

if delivery == "yes":
    extra_delivery = "Delivery Fee: ${:.2f}".format(delivery_cost)
    printed_address = "Delivery Address: {}".format(address)
    printed_phone_number = "Phone number: {}".format(phone_number) # come back to thisssss
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
