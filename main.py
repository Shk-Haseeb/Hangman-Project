import random
import os
import hangman_words
import hangman_art

def clear():
        os.system('clear')

def play_hangman():
    print(hangman_art.logo)
    print("Welcome to Hangman!")
    print("Guess the letters, and try not to get hanged!\n")

    chosen_word = random.choice(hangman_words.word_list)
    word_length = len(chosen_word)
    

    display = ["_"] * word_length
    lives = 6
    guessed_letters = set()

    while True:
        guess = input("Guess a letter: ").lower()
        clear()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter!")
        else:
            guessed_letters.add(guess)
            
            if guess in chosen_word:
                for i in range(word_length):
                    if chosen_word[i] == guess:
                        display[i] = guess
            else:
                lives -= 1
                print(f"Oops! '{guess}' is not in the word. You lost a life.\n")

        print(f"Current word: {' '.join(display)}")
        print(hangman_art.stages[lives])
        print(f"Lives remaining: {lives}\n")

        if "_" not in display:
            print("Congratulations! You guessed the word. You win!\n")
            break

        if lives <= 0:
            print(f"You've run out of lives. The word was '{chosen_word}'. Better luck next time!\n")
            break

if __name__ == "__main__":
    play_hangman()
