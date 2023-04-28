#                                    Exercise 2 - BMI Calculator

#                                           Overview
#                                     My Submissions/Test Runs
#                                          Instructions

#        Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

#        The BMI is a measure of someone's weight taking into account their height.
#         e.g. If a tall person and a short person both weigh the same amount, the
#                    short person is usually more overweight.

#           The BMI is calculated by dividing a person's weight (in kg) by the square
#           of their height (in m):

#            BMI = weight (kg) / height ** 2 ( m ** 2)


# Warning you should convert the result to a whole number.

#        Example Input
#         weight = 80
#         height = 1.75

#        Example Output
#        80 ÷ (1.75 x 1.75) = 26.122448979591837
#        26


# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

individual_height_as_float = float(height)
individual_weight_as_int = int(weight)

bmi_calculator_as_float = individual_weight_as_int / (individual_height_as_float ** 2)
bmi_calculator_as_int = int(bmi_calculator_as_float)
print(bmi_calculator_as_int)
