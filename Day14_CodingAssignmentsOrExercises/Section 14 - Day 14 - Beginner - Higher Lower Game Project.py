from art import logo,versus_logo

from game_data import data
import random

def clear() -> None:
    """Clear the terminal."""
    print('\n' * 100)


def get_random_account():
    """Get data from random account"""
    return random.choice(data)


def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(versus_logo)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()


'''
 
def calculate_and_compare_followers_for_A_and_B(userChoice, followers_for_first_celebrity, followers_for_second_celebrity,country_for_first_celebrity,country_for_second_celebrity,profession_for_first_celebrity,profession_for_second_celebrity,name_for_first_celebrity,name_for_second_celebrity):
    user_score = 0
    is_game_over = False

    while not is_game_over:
        if followers_for_first_celebrity > followers_for_second_celebrity:
            user_score += 1
        elif userChoice == 'B':
            if followers_for_second_celebrity > followers_for_first_celebrity:
                user_score += 1
        print(logo)
        print(f"You're right! Current score: {score}.")
        print(f"Compare A: {name_for_first_celebrity}, a {profession_for_first_celebrity}, from {country_for_first_celebrity}")
        print(versus_logo)
        print(
            f"Against B: {name_for_second_celebrity}, a {profession_for_first_celebrity}, from {country_for_second_celebrity}")
        user_input = input("Who has more followers? Type'A' or 'B': ")
        if userChoice == 'A':






            return user_score
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final Score: {user_score}")

            return user_score
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final Score: {user_score}")
    else:
        is_game_over = True








def play_higher_lower_game():
    """" Plays the higher lower game"""

    # Generate random numbers in order to print the dictionary from the list
    generate_random_number_first_set = random.randint(0, 49)
    generate_random_data_list = data[generate_random_number_first_set]

    entry = generate_random_data_list
    first_celebrity_name = entry["name"]
    first_celebrity_profession = entry["description"]
    first_celebrity_country = entry["country"]
    first_celebrity_followers = entry["follower_count"]

    shuffle_data_list = []

    for each_data in range(0, 49):
        shuffle_data_list.append(random.choice(data))

    random.shuffle(shuffle_data_list)
    generate_random_number_second_set = random.randint(0, 49)
    shuffle_data_list = data[generate_random_number_second_set]

    second_entry = shuffle_data_list
    second_celebrity_name = second_entry["name"]
    second_celebrity_profession = second_entry["description"]
    second_celebrity_country = second_entry["country"]
    second_celebrity_followers = second_entry["follower_count"]

    print(logo)
    print(f"Compare A: {first_celebrity_name}, a {first_celebrity_profession}, from {first_celebrity_country}")
    print(versus_logo)
    print(f"Against B: {second_celebrity_name}, a {second_celebrity_profession}, from {second_celebrity_country}")
    user_input = input("Who has more followers? Type'A' or 'B': ")

    # Testing code
    print(user_input)

    calculate_and_compare_followers_for_A_and_B(userChoice=user_input, followers_for_first_celebrity=first_celebrity_followers,
                                    followers_for_second_celebrity=second_celebrity_followers,country_for_first_celebrity=first_celebrity_country,profession_for_first_celebrity=first_celebrity_profession, name_for_first_celebrity=first_celebrity_name,country_for_second_celebrity=second_celebrity_country,profession_for_second_celebrity=second_celebrity_profession, name_for_second_celebrity=second_celebrity_name)





play_higher_lower_game()
  
'''