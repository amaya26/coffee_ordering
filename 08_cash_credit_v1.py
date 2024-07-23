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

while True:
    payment_method = cash_credit("Would you like to pay with cash or credit? ")
    print(payment_method)
