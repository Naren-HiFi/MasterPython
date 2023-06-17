f_number = int(input("Enter the first number: \n"))
s_number = int(input("Enter the second number: \n"))

def my_function_with_output(firstNumber,secondNumber):
    result = firstNumber * secondNumber
    return result

output = my_function_with_output(firstNumber = f_number,secondNumber = s_number)
print(output)

first_name = input("Enter your first name: \n")
last_name = input("Enter your last name: \n")
def format_name(first_name,last_name):
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    return f"The full name of the user is {formatted_first_name} {formatted_last_name}"

formatted_string = format_name(first_name,last_name)
print(formatted_string)

'''

first_name = input("Enter your first name: \n")
last_name = input("Enter your last name: \n")

def format_name(first_name,last_name):
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    print(f'The full name of the user is {formatted_first_name} {formatted_last_name}')

format_name(first_name,last_name)

'''