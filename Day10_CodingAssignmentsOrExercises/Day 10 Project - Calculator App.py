'''
                                 Day 10 - Functions with Outputs
                                     Calculator App
'''

from art import logo


def add(firstNumber, SecondNumber):
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

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for operator in dict_operations:
        print(operator)

    isCalculationToBeContinued = False

    while not isCalculationToBeContinued:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = dict_operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')

        continue_calculation = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
        if continue_calculation == "y":
            num1 = answer
        else:
            isCalculationToBeContinued = True
            calculator()

calculator()









