from game_data import data
import random
from art import logo, vs
from replit import clear


def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]

    return (f"{account_name}, a {account_desc}, from   {account_country}")


def check(guess, a_fol, b_fol):
    if a_fol > b_fol:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against: {format_data(account_b)}")

    guess = input("Which one is higher? A or B? \n").lower()

    a_fol = account_a["follower_count"]
    b_fol = account_b["follower_count"]
    is_correct = check(guess, a_fol, b_fol)
    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}. ")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong! Final score: {score}.  ")
        should_cont = input("Do you want to play again? Y or N \n")
        if should_cont == "Y":
            score = 0
            game_should_continue = True
        else:
            game_should_continue = False
