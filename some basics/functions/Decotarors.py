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