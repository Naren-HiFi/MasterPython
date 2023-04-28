#
#      Mathematical Operations In Python           PEMDAS                     PEMDASLR
#               3 + 5                             Parentheses          ()     ()
#               7 - 4                             Exponents            **     **
#               3 * 2                             Multiplication       *      */ (Equally important)
#       6 / 3 => Gives the floating value         Division             /      +- (Equally important)
#               3 ** 3                            Addition             +
#                                                 Subtraction          -


#                             Addition of two numbers
add_num = 3 + 5
print('Addition of two numbers: '+ str(add_num))

#                            Subtraction of two numbers
sub_num = 7 - 4
print('Subtraction of two numbers: '+ str(sub_num))

#                             Multiplication of two numbers
mul_num = 3 * 2
print('Multiplication of two numbers: '+ str(mul_num))

#                              Division of two numbers
div_num = 12 / 6
int_num = int(div_num)
print('Division of two numbers: '+ str(int_num))

#                              Power of numbers
add_num = 3 ** 3
print('Power of numbers: '+ str(add_num))

#                                 PEMDAS
print(3 * 3 + 3 / 3 - 3)
print(3 * 3 + 3 / 3 - 7)
print(3 * (3 + 3) / 3 - 3)