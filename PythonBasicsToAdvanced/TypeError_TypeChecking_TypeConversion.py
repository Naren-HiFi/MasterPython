# num_char = len(input("What is your name?\n"))
# print("Your name has "+num_char+" characters")

# You will get the TypeError when you run the code above

# Traceback (most recent call last):

#  File
#  "E:\Udemy_Angela_Python_From_Scratch\PythonBasicsToAdvanced\
#  TypeError_TypeChecking_TypeConversion.py", line 2, in <module>

#    print("Your name has "+num_char+" characters")
#          ~~~~~~~~~~~~~~~~^~~~~~~~~
# TypeError: can only concatenate str (not "int") to str


# Print the input length of the characters
num_char = len(input("What is your name?\n"))

# Checks the type of the data using type() function
print(type(num_char))

# Converts the integer to string using str() function. This is called TypeConversion
new_num_char = str(num_char)

# print the number of characters in your name
print("Your name has "+ new_num_char +" characters")


a = str(123)
print(type(a))

print(70 + float("100.5"))

print(str(70)+str(100))
