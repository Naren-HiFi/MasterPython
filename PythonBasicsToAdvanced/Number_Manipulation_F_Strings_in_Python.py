num_one = 8
num_two = 3

number_one = 10
number_two = 3

# Dividing the number returns the float value
float_num = num_one/num_two
print(float_num)

# int function will convert the float into a whole number
int_whole = int(float_num)
print(int_whole)


# Round Function is used to round the decimal or float values upto one, two or three decimal places
round_num = round(num_one/num_two)
print(round_num)

# Round the number to 3 decimal places
round_num = round(num_one/num_two, 3)
print(round_num)

#  // is used to give the whole number
double_forward_slash_number = num_one // num_two
print(double_forward_slash_number)


print(number_one/number_two)
round_number = round(number_one/number_two)
print(round_number)

result = 4 / 2
result /= 2
print(result)

result = 4 // 2
result //= 2
print(result)

#    In Python, an f-string is a string literal that is prefixed
#    with the letter "f". F-strings allow you to embed expressions such as boolean, integer, and
#    float inside string literals, using curly braces {}.

#             F-strings were introduced in Python 3.6 and
#             are a powerful way to create formatted strings in Python

#             For example, consider the following code snippet:

int_score = 100
float_height = 7.8
isWinning = True

# f-String
print(f'Your score is {int_score}, Your height is {float_height}, Are you winning? {isWinning}')

