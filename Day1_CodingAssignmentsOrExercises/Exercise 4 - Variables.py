"""

Instructions

Write a program that switches the values stored in the variables a and b.

Warning. Do not change the code on lines 1-4 and 12-18.

Your program should work for different inputs. e.g. any value of a and b.

Example Input
a: 3
b: 5

Example Output
a: 5
b: 3

e.g. When you hit run, this is what should happen:


Hint

You should not have to type any numbers in your code.

You might need to make some more variables.

"""

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# Swap the values of existing by defining and assigning values to new two variables
c = a
d = b
a = d
b = c

"""
Alternate Solution

c = a
a = b
b = c

"""


#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
