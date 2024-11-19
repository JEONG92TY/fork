def alphabetize_words():
    print("enter a list of words separated by spaces:")
    user_input = input("words: ")
    
    words = user_input.split()
    
    sorted_words = sorted(words)
    
    print("\nwords in alphabetical order:")
    for word in sorted_words:
        print(word)

alphabetize_words()

