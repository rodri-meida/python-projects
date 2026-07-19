menu = ({"Hot Dog": 2.50,"Hamburger": 3.00,"Fries": 1.50,"Soda": 1.00,"Water": 0.75,})

while True:
    print(menu)
    order = (str(input("What you like to order from the menu?(q to quit):")))
    if order == menu:
        print(f"You have selected {order}! Anything else?")
    elif order == "q":
        print("Quiting...")
        break 
    elif order == "":
        print("You have selected nothing! Pick something or quit(type q)! ")
    
    else:
        continue

print("---Your Cart---")

for order in menu:
    for menu in total:
        print(menu)
