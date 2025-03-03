# In Python a function is defined using the def keyword:
a=20
b=30
# creating the function
def my_function():
    print("hello world")

# calling the function
my_function()


#creating function with arguments
def function_argu(fname):
    print("my name is "+fname)

#passing an argument
function_argu("nabin")
#

# function to calculate sum with parameters  
def sum(x,y):
    add=x+y
    print(add)
    return add

# calling the function which name is sum
result=sum(a,b)
print(result)

# By default, a function must be called with the correct number of 
# arguments. Meaning that if your function expects 2 arguments, you have 
# to call the function with 2 arguments, not more, and not less.

# If you do not know how many arguments that will be passed into your 
# function, add a * before the parameter name in the function definition.

def my_kids(*kids):
    print("i have many child among them eldest is "+kids[0])

my_kids("nabin","ram","shyam")

# You can also send arguments with the key = value syntax.
def my_childs(child1,child2,child3):
    print("my childs are "+child1+","+child2+","+child3)

my_childs(child1="hem",child3="ayush",child2="mohit")


# If you do not know how many keyword arguments that will be passed into 
# your function, add two asterisk: ** before the parameter name in the
#  function definition.

def key_arguments(**kid):
    print("his last name is "+kid["lname"])

key_arguments(fname="nabin",lname="basnet")

# defaunt parameters
def default_parameters(country="nepal"):
    print("i am from "+country)

default_parameters("USA")
default_parameters()


# returm value
def return_val(x):
    return 5*x

print(return_val(5))