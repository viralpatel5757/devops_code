#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

print(logo) 
print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")

computer_choice = random.randint(1,100)
print(f"Pssst, the correct answer is {computer_choice}")

stop_game = False

def compare():
    user_choice = int(input("make a guess: "))
    if user_choice > computer_choice:
        print("Too heigh !!")
    elif user_choice < computer_choice:
        print("Too Low !!")
    elif user_choice == computer_choice:
        print(f"You won !! the correct answer was {computer_choice}") 
        global stop_game
        stop_game = True

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
i = 0
if difficulty == "easy":
    while i < 10 and not stop_game :
        compare()
        print(f"you have {9 - i} attempts remaining") 
        if i-9 == 0 and not stop_game:
            print("Game over!! you lose")
        i += 1    
elif difficulty == "hard":
    while i < 5 and not stop_game :
        compare()
        print(f"you have {4 - i} attempts remaining")
        if i-4 == 0 and not stop_game:
            print("Game over!! you lose")
        i += 1    