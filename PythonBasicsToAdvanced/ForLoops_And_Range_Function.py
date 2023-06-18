# For Loop With Range

# For loop and range() to print the numbers from 1 to 10
for number in range(1,11):
    print(number)

# For loop, range() and increment (1, 11, 3) to print the numbers from 1 to 10
for number in range(1, 11, 3):
    print(number)

# For loop, range(1, 101) to add the numbers from 1 to 100. The sum of the numbers from 1 t0 100 is 5050
total_sum_of_hundred_numbers = 0;
for number in range(1, 101):
    total_sum_of_hundred_numbers += number
print(total_sum_of_hundred_numbers)

# For loop and range() to print the even numbers from 2 to 100
for even_numbers in range(2,101):
    if(even_numbers % 2 == 0):
      print(even_numbers)


def prime_checker(number):

    is_Prime = True

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                is_Prime = False
        if is_Prime:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

