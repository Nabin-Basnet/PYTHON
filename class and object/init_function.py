
# self in Python is like a way for an object to talk about itself. It's used inside a
#  class to refer to the object that is using the method. For example, if an object 
# wants to access its own data or call its own methods, it uses self.

# __init__ is a special method, also known as a constructor. It is automatically
#  called when an object of a class is created. You use it to initialize the object's
#  attributes (set up its data) when the object is created.
class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=person("nabin",20)
print(f"my name is {p1.name} and i am {p1.age}")