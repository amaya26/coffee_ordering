def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))
            return response

        except ValueError:
            print(error)


phone_number = num_check("What is your phone number?", "Please enter a number.", int)
print(phone_number)