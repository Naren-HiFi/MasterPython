# Creating a dictionary named programming_dictionary
programming_dictionary = {
 "Bug": "An error in a program that prevents the program from running as expected.",
 "Function": "A piece of code that you can easily call over and over again."
}

# Retrieving items from dictionary
#print(programming_dictionary["Function"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
#print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}
#
# Wipe an existing diictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in the dictionary
programming_dictionary["Bug"] = "A moth in your computer."
#print(programming_dictionary)

# Loop through the dictionary
for key in programming_dictionary:
    print("\n")
    # Prints the key present in the dictionary
    print(key)
    print("\n")
    # Prints the value present in the dictionary
    print(programming_dictionary[key])
