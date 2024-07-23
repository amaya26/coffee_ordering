while True:
    confirm_cancel = input("\nPlease cancel or confirm your order. ").lower()
    if confirm_cancel == "cancel":
        print("Order cancelled. ")
        exit()
    elif confirm_cancel == "confirm":
        print("Your order is being processed now.")
        break
    else:
        print("Please type either cancel or confirm. ")