# Simple Function
print("This is the simple function \n")
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")

greet()

print("\n")

# Function that allows for input
print("This is the function with arguments and parameters \n")
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")
    print(f"Isn't the weather nice today?, {name}")

greet_with_name('Kiran')
