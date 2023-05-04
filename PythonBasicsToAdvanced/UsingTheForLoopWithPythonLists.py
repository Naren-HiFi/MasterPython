# Create a fruits list with three items
fruits = ["Apple", "Peach","Pear"]
print(type(fruits))
# Iterate the fruits list using for loop and print the fruits list
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
    print(f"{fruit} juice")
    print(fruits)  # The fruits list is printed thrice because it's indented inside the for loop
print(fruits)  # The fruits list is printed once because it's indented outside the for loop
