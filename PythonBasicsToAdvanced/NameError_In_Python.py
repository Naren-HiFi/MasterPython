def a_function(a_parameter):
    a_variable = 15
    #print(a_variable)
    return a_parameter

a_function(10)
print(a_variable)

"""

The code will result in a NameError with the message "name 'a_variable' is not defined".

Explanation:

The function a_function() takes a single parameter a_parameter and returns the value of a_parameter.

Inside the function, a new variable a_variable is defined and assigned the value 15.

When the function is called with a_function(10), it returns the value 10, but this value is not saved or printed.

After the function call, the print() function tries to print the value of a_variable, which 
is not defined outside the function.

Therefore, the code raises a NameError because a_variable is not defined in the current scope.

"""