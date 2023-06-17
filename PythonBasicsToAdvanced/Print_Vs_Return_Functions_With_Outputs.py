#                                        Calculator
def add(firstNumber,SecondNumber):
    """ Adds the two given input numbers """
    return firstNumber + SecondNumber
def subtract(firstNumber, SecondNumber):
    """ Subtracts the two given input numbers """
    return firstNumber - SecondNumber
def multiply(firstNumber, SecondNumber):
    """ Multiplies the two given input numbers """
    return firstNumber * SecondNumber
def divide(firstNumber, SecondNumber):
    """ Divides the two given input numbers """
    return firstNumber / SecondNumber

dict_operations = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for operator in dict_operations:
    print(operator)

operation_symbol = input("Pick an operation from the line above: ")
calculation_function = dict_operations[operation_symbol]
first_answer = calculation_function(num1,num2)

print(f'{num1} {operation_symbol} {num2} = {first_answer}')

operation_symbol = input("Pick an another operation: ")
num3 = int(input("What's the next number?: "))
calculation_function = dict_operations[operation_symbol]
second_answer = calculation_function(calculation_function(num1,num2),num3)

print(f'{first_answer} {operation_symbol} {num3} = {second_answer}')


