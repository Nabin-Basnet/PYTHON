# Decorators let you add extra behavior to a function, without changing the function's code.
#A decorator is a function that takes another function as input and returns a new function.


def initalgreet(func):
    func()
    def wrapper():
        print("hello! babe")
    
    return wrapper


@initalgreet
def finalgreet():
    print("how are you")

finalgreet()

#multiple decorators

def greet(func):
    def dogreet():
        print("Namastey !")
    func()
    return dogreet
@greet
def intro():
    print("mero nam nabin basnet ho.")


intro()
    
@greet
def question():
    print("what about you?")

question()

def calculate(fun):
    def sum(a,b):
        print(f"sum is {a+b}")
        fun()
    return sum

@calculate
def explain():
    print("here we did sum")


explain(3,2)