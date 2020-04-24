#options =
import random

comp_input = random.choice(['rock','paper','scissor'])
user_input = ""
user_check = False
while user_check is False:
    user_input = input("Make your choice: ")
    if not (user_input.lower() in ['rock', 'paper', 'scissor']):
       print ("Make a valid choice")
    elif user_input.lower() == comp_input.lower():
        print("Opposing Choice is: " + comp_input)
        print ("You are tied. Try again")
        comp_input = random.choice(['rock', 'paper', 'scissor'])
    elif user_input.lower() == "rock":
        print("Opposing Choice is: " + comp_input)
        if comp_input == "paper":
            print("You lose! Paper beats Rock")
        elif comp_input == "scissor":
            print("You win! Rock beats Scissor")
        user_check = True
    elif user_input.lower() == "scissor":
        print("Opposing Choice is: " + comp_input)
        if comp_input == "paper":
            print("You Win! Scissor beats Paper")
        elif comp_input == "rock":
            print("You Lose! Rock beats Scissor")
        user_check = True
    elif user_input.lower() == "paper":
        print("Opposing Choice is: " + comp_input)
        if comp_input == "scissor":
            print("You Lose! Scissor beats Paper")
        elif comp_input == "rock":
            print("You Win! Paper beats Rock")
        user_check = True