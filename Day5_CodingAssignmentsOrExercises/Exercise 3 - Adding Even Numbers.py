
'''
i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output.

It should just print the final total and not every step of the calculation.

Hint

There are quite a few ways of solving this problem, but you will need to
use the range() function in any of the solutions.

'''

#Write your code below this row 👇
sum_of_even_numbers = 0

for even_numbers in range(2,101):
    if(even_numbers % 2 == 0):
      sum_of_even_numbers += even_numbers
print(sum_of_even_numbers)

# Alternate Solution

#Write your code below this row 👇
total = 0
for number in range(2,101,2):
      total += number
print(total)
