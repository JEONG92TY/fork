import random

number = random.randint(1, 100)
print("i'm thinking of a number between 1 and 100")

while True:
    guess = int(input("enter your guess: "))
    if guess < number:
        print("too low!")
    elif guess > number:
        print("too high!")
    else:
        print("congratulations!")
        break
