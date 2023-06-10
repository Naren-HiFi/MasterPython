'''
               Day 7 Project (Hangman) - For & While Loops, If Else, Lists, Strings, Range, And Modules



'''

# Step 5

import random

import os

def clear_console():
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For Linux and Mac
        _ = os.system('clear')

'''
The os module provides a way to interact with the operating system, and the system function allows you to execute commands in the console.

The clear_console function checks the operating system using os.name and then executes the appropriate command to clear the console.

On Windows, the command is cls, and on Linux and Mac, it's clear.

You can place this code at any point in your Python script, and when executed, it will clear the console in PyCharm.

'''

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo

print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Call the clear_console function whenever you want to clear the console
    clear_console()

    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    from hangman_art import stages

    print(stages[lives])