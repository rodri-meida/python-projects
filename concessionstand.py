#Variables of the engine
menu = ({"Hot Dog": 2.50,"Hamburger": 3.00,"Fries": 1.50,"Soda": 1.00,"Water": 0.75,})
cart = []
total = 0

#Engine
while True: 
    print(menu)
    order = (str(input("What you like to order from the menu?(q to quit):")))
    if order == "q" "Q":
        print("Quiting...")
        break 
    elif order == "":
        print("You have selected nothing! Pick something or quit(type q)! ")
    elif order in menu:
        cart.append(order)
        print(f"You have selected {order}! Anything else?")
    else:
        print("That item isn't in the menu.")

#Finishing 
print("---Your Cart---")

for order in cart:
    print(order)

print("---Price of your cart---")

for order in total:
    print(order) 
#Works
