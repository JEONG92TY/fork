# print("hello, world!")
import random

choices = ["rock", "paper", "scissors"]
user_choice = input("choose rock, paper, or scissors: ").lower()
computer_choice = random.choice(choices)

print(f"computer chose: {computer_choice}")
if user_choice == computer_choice:
    print("it's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("you win!")
else:
    print("you lose!")
