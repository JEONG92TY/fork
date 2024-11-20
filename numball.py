import random

def generate_number():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]

def get_feedback(guess, target):
    strikes, balls = 0, 0
    for i, g in enumerate(guess):
        if g == target[i]:
            strikes += 1
        elif g in target:
            balls += 1
    outs = len(guess) - strikes - balls
    return strikes, balls, outs

def main():
    print("guess the 3-digit number: all digits are different")    
    target = generate_number()
    attempts = 0

    while True:
        user_input = input("enter your guess: ")
        if len(user_input) != 3 or not user_input.isdigit() or len(set(user_input)) != 3:
            print("invalid input: enter 3 unique digits")
            continue
        
        guess = [int(digit) for digit in user_input]
        attempts += 1
        strikes, balls, outs = get_feedback(guess, target)

        print(f"result: {strikes} strike(s), {balls} ball(s), {outs} out(s)")
        
        if strikes == 3:
            print(f"congratulations! ({attempts} attempts)")
            break

if __name__ == "__main__":
    main()
