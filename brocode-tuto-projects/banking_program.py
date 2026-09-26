# setting a global variable
balance = 1000

# setting functions
def stats_balance():
    print(f"Your balance is ${balance:.2f}")


def do_deposit():
    global balance
    deposit = input("You would like to deposit money to your bank account (y/n)? ").strip().lower()
    if deposit == "y":
        try:
            quantity_deposit = int(input("How much money do you want to deposit? "))
        except ValueError:
            print("Please enter a valid number.")
            return

        if quantity_deposit <= 0:
            print("You can't deposit $0 or lower! Pick a valid quantity!")
        else:
            balance += quantity_deposit
            print(f"You have deposited ${quantity_deposit}!")
    else:
        print("No deposit made.")


def send_money():
    global balance
    send_cash = input("What service would you like to send money? ").strip().lower()

    if send_cash == "taxes":
        try:
            taxes_send = float(input("How much do you need to pay taxes?: "))
        except ValueError:
            print("Please enter a valid number.")
            return

        if taxes_send <= 0:
            print("You can't send $0 or lower! Pick a valid quantity!")
        elif taxes_send > balance:
            print("You don't have enough money! Try to deposit more money to pay your taxes!")
        else:
            balance -= taxes_send
            print("You have paid your taxes!")
    else:
        print("Service not recognized. Try 'taxes'.")

# inicial screen

while True:
    print("###############")
    print("Banking Program")
    print("###############")
    print("1:Deposit")
    print("2:Balance")
    print("3:Send Money")
    print("4:Quit")
    try:
        option = int(input("What you would you like to do? "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if option == 1:
        do_deposit()
    elif option == 2:
        stats_balance()
    elif option == 3:
        send_money()
    elif option == 4:
        print("Quiting the app...")
        break
    else:
        print("Please choose an option from 1 to 4.")
    
    



