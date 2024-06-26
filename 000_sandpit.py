def cash_credit(question):
    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            return "cash"

        elif response == "credit" or response == "cr":
            payment_surcharge = 5
            print("Card payment surcharge: {}".format(payment_surcharge))
            return "credit"

        else:
            print("Please enter a valid payment method")

cash_credit("What would you like to play by? (cash or credit)")