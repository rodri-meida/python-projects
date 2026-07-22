#imported random module
import random

choices = ["rock", "paper", "scissors"]


is_running = True

while is_running is True :
    print("Rock, Paper, Scissors Python Game")
    pc = random.choice(choices)
    player = (str(input("Pick between rock, paper and scissors!(input q to quit if u want):")))
    if player == "q":
        print("Quitting...")
        break
    elif pc == player:
        print("It is a draw! Play again!")
    elif pc == "rock":
        if player == "paper":
            print(f"Bot chosed {pc}! You win!")
        elif player == "scissors":
            print(f"Bot chosed {pc}! You lose!")
    elif pc == "paper":
        if player == "scissors":
            print(f"Bot chosed {pc}! You win!")
        elif player == "rock":
            print(f"Bot chosed {pc}! You lose!")
    elif pc == "scissors":
        if player == "rock":
            print(f"Bot chosed {pc}! You win!")
        elif player == "paper":
            print(f"Bot chosed {pc}! You lose!")
    else:
        print("That input isnt available! Pick between rock, paper, scissors please.")

    