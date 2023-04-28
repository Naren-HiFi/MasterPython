#                            Instructions

#       I was reading this article by Tim Urban - Your Life in Weeks and realised
#       just how little time we actually have.

#              https://waitbutwhy.com/2014/05/life-weeks.html

#            Create a program using maths and f-Strings that tells us how many days, weeks, months
#             we have left if we live until 90 years old.

#       It will take your current age as the input and output a message with our time left
#       in this format:

#       You have x days, y weeks, and z months left.

#       Where x, y and z are replaced with the actual calculated numbers.

#            Warning your output should match the Example Output format exactly,
#            even the positions of the commas and full stops.

                            # Example Input
                            # 56

                           # Example Output
                           # You have 12410 days, 1768 weeks, and 408 months left.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Convert the string to int
age_as_integer = int(age)

# Find the difference between the 90 and your age
final_years_left = 90 - age_as_integer

# Multiply the remaining years with 365 days, 52 weeks, and 12 months
final_days_left = 365 * final_years_left
final_weeks_left = 52 * final_years_left
final_months_left = 12 * final_years_left

print(f"You have {final_days_left} days, {final_weeks_left} weeks, and {final_months_left} months left.")



