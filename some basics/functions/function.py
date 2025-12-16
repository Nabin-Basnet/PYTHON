#function is a block of code which is executed when it is call
def name():
    print("my name is nabin")

name()

#a single function can be call multiple time
name()
name()
# Information can be passed into functions as arguments.
def greet(name):
    print(f"hello! my name is {name} basnet")

greet("nabin")


#function returning value
def sum(a,b):
    result=a+b
    return result


x=sum(3,2)
print(x)

# *args and **kwargs
#By default, a function must be called with the correct number of arguments.
# However, sometimes you may not know how many arguments that will be passed into your function.
# *args and **kwargs allow functions to accept a unknown number of arguments.

def func(*kids):
    print(f"my youngest child is {kids[2]}")

func('nabin','rabin','sabin','hari')