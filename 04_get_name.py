# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        # if the response is blank, outputs an error
        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


while True:
    name = not_blank("What is your name? ").capitalize()
    print("{}.".format(name))