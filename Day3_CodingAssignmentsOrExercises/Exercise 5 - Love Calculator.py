"""

                           💪 This is a Difficult Challenge 💪

Instructions

You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2-digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is **z**."

e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

Example Input 1

name1 = "Kanye West"
name2 = "Kim Kardashian"

Example Output 1

Your score is 42, you are alright together.

Example Input 2
name1 = "Brad Pitt"
name2 = "Jennifer Aniston"

Example Output 2

Your score is 73.

"""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_to_lowercase = name1.lower()
name2_to_lowercase = name2.lower()
combined_name = name1_to_lowercase + name2_to_lowercase

count_t = combined_name.count("t")
count_r = combined_name.count("r")
count_u = combined_name.count("u")
count_e = combined_name.count("e")
count_l = combined_name.count("l")
count_o = combined_name.count("o")
count_v = combined_name.count("v")
count_true = count_t + count_r + count_u + count_e
count_love = count_l + count_o + count_v + count_e

true_love_score = str(count_true)+str(count_love)
two_digit_number = int(true_love_score)
if two_digit_number < 10 or two_digit_number > 90:
    print(f"Your score is {two_digit_number}, you go together like coke and mentos.")
elif 40 < two_digit_number < 50:
    print(f"Your score is {two_digit_number}, you are alright together.")
else:
    print(f'Your score is {two_digit_number}.')




