# Functions with more than 1 input

# Function with positional argument
def greet_with(name, location):
    print(f'Hello {name}. What is it like to be in {location}')

greet_with("Nowhere","Kiran")

# Function with keyword argument
def greet_with(name, location):
    print(f'Hello {name}. What is it like to be in {location}')

greet_with(location="Rajapalayam",name="Pattu")
'''

greet_with("Rajapalayam","Pattu") => In python programming, this is called positional argument.

Because we haven't specified anywhere which particular parameter we want to associate these pieces of data with.

So, it's just gone and looked at the position.

Keyword Arguments

def my_function(a,b,c):
    
    # Do this with a
    
my_function(a=1,b=2,c=3)   

my_function(c=4,a=2,b=0)   
 

'''