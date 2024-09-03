


import random


words = {
    "Frontend": "The client-side part of a software application that interacts with users and displays information.",
    "Python": "A versatile and easy-to-read programming language.",
    "Backend": "The server-side part of a software application that handles data processing, storage, and business logic."
}


word, explanation = random.choice(list(words.items()))
guessed = ["_"] * len(word)
attempts = 10

print("Welcome to the POLY CHUDES!")
print(f"Hint: {explanation}")

while attempts > 0:
    print("Word: ", *guessed)
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"Nope. {attempts} attempts left.")

    if "_" not in guessed:
        print(f"Congrats! You guessed the word: {word}")
        break
else:
    print(f"You lost. The word was: {word}")

