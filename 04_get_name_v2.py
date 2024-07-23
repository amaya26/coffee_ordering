name_list = ["Bob"]

# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question).capitalize()

        # if the response is blank, outputs an error
        if response == "":
            print("Sorry this can't be blank. Please try again")
        elif response in name_list:
            print("You have already placed an order under that name. ")
        else:
            return response


while True:
    name = not_blank("What is your name? ")
    print("Hi {}.".format(name))