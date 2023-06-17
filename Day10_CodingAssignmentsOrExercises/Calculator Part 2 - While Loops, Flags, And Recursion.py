#                                        Calculator
from art import logo

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

def calculator():
    print(logo)

    num1 = int(input("What's the first number?: "))

    for operator in dict_operations:
        print(operator)

    isCalculationToBeContinued = False

    while not isCalculationToBeContinued:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calculation_function = dict_operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')

        continue_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
        if continue_calculation == "y":
            num1 = answer
        else:
            isCalculationToBeContinued = True
            calculator()

calculator()

'''

def calculator(): => is a recursive function

A recursive function is a function that calls itself during its execution. 

It solves a problem by breaking it down into smaller subproblems and applying the same function to
 each subproblem.
  
Here's an example of a recursive function in Python:

Python

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

In this example, the factorial function calculates the factorial of a given number n. 

The factorial of a non-negative integer n is the product of all positive integers less than or equal 
to n.

The function uses a base case (n == 0 or n == 1) to terminate the recursion and return a known result.
 
Otherwise, it calls itself with a smaller value (n - 1) and multiplies the current n with the
result of the recursive call. This process continues until it reaches the base case.

Here's an example of calling the factorial function:

python

result = factorial(5)
print(result)  # Output: 120

The function calculates 5!, which is equal to 5 * 4 * 3 * 2 * 1, resulting in 120.

'''








