import random
import my_Pi_Module

# Random module is a python module that makes it easier for us to generate our random numbers
# Generate random integers between 1 and 10
random_integer = random.randint(1,10)
print("Generate random integers between 1 and 10: "+ str(random_integer))

# Prints the value of pi imported from my_Pi_Module.py file
print(f"Pi = {my_Pi_Module.pi}")

#  Generate random floating point numbers => random.random() => Returns the next random floating point
#  between [0.0 to 1.0]
random_float = random.random()
print(f"Generate random floating point numbers: {random_float}")

# How to generate a random decimal number between 0 and 5?
random_float_between_zero_and_five = random.uniform(0,5)
print("Generate random floating point numbers between 0 and 5: "+ str(random_float_between_zero_and_five))

# Python Random choice() Method
# The choice() method returns a randomly selected element from the specified sequence.
# The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
fruits_list = ['Pomegranate','Apple','Red Banana']
print(random.choice(fruits_list))

fruit_items = len(fruits_list)
print(fruit_items)
random_fruit = random.randint(0,fruit_items-1)
print(fruits_list[random_fruit])