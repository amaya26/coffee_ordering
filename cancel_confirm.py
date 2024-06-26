while True:
    confirm_cancel = input("Please cancel or confirm your order? ").lower()
    if confirm_cancel == "cancel":
        exit()
    elif confirm_cancel == "confirm":
        print("You have confirmed your order.")
    else:
        print("Please type either cancel or confirm. ")