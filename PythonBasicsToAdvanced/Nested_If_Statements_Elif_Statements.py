print("Welcome to the roller coaster ride!")
height = int(input("What's your height in cm? "))
if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    # Nested If Statements
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

print("Welcome to the roller coaster ride!")
height = int(input("What's your height in cm? "))
if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    # elif Statements
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    elif age < 22:
        print("Please pay $10.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
