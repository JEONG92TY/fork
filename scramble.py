import random

words = ["apple", "strawberry", "blueberry", "orange", "watermelon", "grape", "peach"]
word = random.choice(words)
scrambled = ''.join(random.sample(word, len(word)))

print("unscramble the word!")
print(f"scrambled word: {scrambled}")
guess = input("your guess: ")

if guess == word:
    print("correct!")
else:
    print(f"sorry, the correct word was: {word}")
