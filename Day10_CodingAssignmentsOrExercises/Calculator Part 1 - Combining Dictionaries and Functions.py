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
answer = calculation_function(num1,num2)

print(f'{num1} {operation_symbol} {num2} = {answer}')
