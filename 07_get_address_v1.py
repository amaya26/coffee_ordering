
while True:
    address = input("What is your address? ")
    number = any(map(str.isdigit, address))
    string = any(map(str.isalpha, address))
    if number == True and string == True:
        print("Program continues. ")

    else:
        print("Please enter a valid address. ")
