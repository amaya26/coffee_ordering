# checks a response has a valid input
def get_response(question, valid_responses, error):
    while True:
        response = input(question).lower()

        if response in valid_responses:
            return response

        else:
            print(error)

while True:
    answer = get_response("Yes or no? ", ["yes", "no", "y", "n"], "Please enter yes or no. ")
    if answer == "yes" or answer == "y":
        print("yes")
    else:
        print("no")