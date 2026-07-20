#import random module
import random 
#setting up variables
low = 1 
high = 100
guesses =+ 1

number = random.randint(low, high)

#Engine
while True:
    guess = (int(input("What number am I thinking? (1---100):")))
    if guess < 1 or guess > 100:
        print(f"Your number is out of range! Pick a number between {low} and {high}.")
    elif guess < number:
        print(f"My number is higher than {guess}")
    elif guess > number:
        print(f"My number is lower than {guess}")
    else:
        print(f"My number is {guess}! You won!!!")
        print(f"Number of guesses taken:{guesses}")
        break
    
