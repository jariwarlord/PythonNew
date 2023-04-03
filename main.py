from art import logo
import random

print(logo)
level = input("Choose a difficulty. Type 'easy' or 'hard': \n ")
number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100 \n"))

if(level == "easy"):
  turns = 10
elif(level == "hard"):
  turns = 5
  
while number != guess:
    if turns == 0:
        print(f"You have {turns} turns left")
        break
    else:
        turns = turns - 1
        if guess > number:
            print(f"Too High you have {turns} turns left")
            guess = int(input("Guess a number between 1 and 100 \n"))

        elif number > guess:
            print(f"Too Low youh have {turns} turns left")
            guess = int(input("Guess a number between 1 and 100 \n"))

else:
    print(f"You win ! Answer was: {number}!")

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
