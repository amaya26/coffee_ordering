def num_check(question, error):
    valid = False
    while not valid:

        response = input(question)
        if response.isdigit():
            return response
        else:
            print(error)


phone_number = num_check("What is your phone number? ", "Please enter a number.")
print(phone_number)