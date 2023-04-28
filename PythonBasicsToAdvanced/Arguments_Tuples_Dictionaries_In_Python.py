def all_aboard(a, *args, **kw):
    print(a, args, kw)

all_aboard(4, 7, 3, 0, x=10, y=64)

'''

The output of the code will be: 4 (7, 3, 0) {'x': 10, 'y': 64}

Explanation:

The function all_aboard() has three parameters: a, *args, and **kw.

The *args parameter allows the function to accept an arbitrary number of positional arguments, which 
are packed into a tuple.

The **kw parameter allows the function to accept an arbitrary number of keyword arguments, which 
are packed into a dictionary.

When all_aboard(4, 7, 3, 0, x=10, y=64) is called, the value 4 is assigned to the a parameter, 7, 3, and 0 
are packed into a tuple and assigned to the *args parameter, while x=10 and y=64 are packed into a dictionary
and assigned to the **kw parameter.

When the print() function is called inside all_aboard(), it prints the values of a, args, and kw.

Therefore, the output of the code will be: 4 (7, 3, 0) {'x': 10, 'y': 64}

Tuple

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data,
 the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

'''