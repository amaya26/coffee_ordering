

# checks a response has a valid input
def get_response(question, valid_responses, error):
    while True:
        response = input(question).lower()

        if response in valid_responses:
            return response

        else:
            print(error)

while True:
    answer = yes_no("yes or no? ", ["yes", "y", "n", "no"], "error please enter yes or no")
    print(answer)

    cash_credit = yes_no("how do you want to pay?", ["cash", "credit"], "error plkease enter cash or credit")
