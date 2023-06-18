import random
from art import logo

EASY_NO_OF_ATTEMPTS = 10
HARD_NO_OF_ATTEMPTS = 5

#Function to check user's guess against actual answer.
def check_answer(user_guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if user_guess < answer:
        print("Too low.")
        return turns - 1
    elif user_guess > answer:
        print("Too high.")
        return turns - 1
    elif user_guess == answer:
        print(f"You got it! The answer was {answer}")
def set_difficulty():
    """ Make function to set difficulty. """
    game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if game_difficulty == "easy":
        return EASY_NO_OF_ATTEMPTS
    else:
        return HARD_NO_OF_ATTEMPTS

def guess_number():
    """" Choosing a random number between 1 and 100."""
    print(logo)
    # Choosing a random number between 1 and 100.
    welcome_message = "Welcome to the Number Guessing Game! \n"
    print(welcome_message)
    game_message = "I'm thinking of a number between 1 and 100. \n"
    print(game_message)
    answer = random.randint(1, 100)
    print(f'Pssst, the correct answer is {answer}')

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    user_guess = 0
    while user_guess != answer:
        print(f'You have {turns} attempts remaining to guess the number.')

        # Let the user guess a number.
        user_guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(user_guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif user_guess != answer:
            print("Guess again.")


guess_number()






