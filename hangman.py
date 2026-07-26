import random

def choose_word():
    words = ["python", "hangman", "computer", "keyboard", "program"]
    return random.choice(words)

def play_hangman():
    word = choose_word()
    guessed_letters = []
    attempts_left = 6
    word_display = ["_"] * len(word)

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters. You have {attempts_left} wrong guesses allowed.\n")

    while attempts_left > 0 and "_" in word_display:
        print("Word: " + " ".join(word_display))
        print(f"Attempts left: {attempts_left}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already tried that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!\n")
            for i in range(len(word)):
                if word[i] == guess:
                    word_display[i] = guess
        else:
            attempts_left -= 1
            print("Wrong guess!\n")

    if "_" not in word_display:
        print("You guessed it! The word was:", word)
    else:
        print("Out of attempts! The word was:", word)

if __name__ == "__main__":
    play_hangman()