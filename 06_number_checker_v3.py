# checks that the phone number only contains numbers
def num_check(question, error):
    while True:
        response = input(question)  # get user input
        if response.isdigit() and 7 <= len(response) <= 15:  # if input is a number between 7 and 15
            print("Program continues")
            return response
        else:  # if input not valid
            print(error)  # print an error message

while True:
    phone_number = num_check("Phone number: ", "Error")


