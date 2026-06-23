import random

words = ["apple", "tiger", "house", "flower", "python"]

secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("===== HANGMAN GAME =====")

while wrong_guesses < max_wrong:
    display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("\nCongratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong!")
        print("Remaining chances:", max_wrong - wrong_guesses)

if wrong_guesses == max_wrong:
    print("\nGame Over!")
    print("The correct word was:", secret_word)
