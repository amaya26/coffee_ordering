# functions go here


# main routine goes here
while True:
    want_instructions = input("Do you want to view the menu? ").lower()

    if want_instructions == "yes":
        print("Menu goes here")
    elif want_instructions == "no":
        pass
    else:
        print("Please answer yes / no")

print("We are done")