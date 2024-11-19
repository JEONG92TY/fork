import random

number = random.randint(1, 100)
print("i'm thinking of a number between 1 and 100")

attempts = 5

while attempts > 0:
    guess = int(input(f"enter your guess ({attempts} attempts left): "))
    
    if guess < number:
        print("too low!")
    elif guess > number:
        print("too high!")
    else:
        print("congratulations!")
        break  
    
    attempts -= 1  

if attempts == 0:
    print(f"sorry, the number was >{number}<")
