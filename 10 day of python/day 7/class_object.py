# # python is an object oriented programming language.
# # Almost everything in Python is an object, with its properties and methods.
# # A Class is like an object constructor, or a "blueprint" for creating objects.

# class person:
#     # The __init__() function is called
#     #  automatically every time the class is 
#     # being used to create a new object.
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     # The __str__() function controls what should 
#     # be returned when the class object is represented as a string.
#     def __str__(self):
#         return f"{self.name} {self.age}"
    

#     # Insert a function that prints a greeting, and
#     #  execute it on the p1 object:
#     def greeting(self):
#         print(f"hello {self.name} how are you")

# p1=person("nabin",20)
# print(p1)
# p1.greeting()
# print(p1.name)
# print(p1.age)
    
# #  The self parameter is a reference to the current instance of
# #  the class, and is used to access variables that belong to the class.
# # It does not have to be named self, you can call it whatever you 
# # like, but it has to be the first parameter of any function in the class:   
# class Persons:
#   def __init__(mysillyobject, name, age):  #__init__ function will always executed no matter whether it is call or not 
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Persons("John", 36)
# p1.myfunc()



class person():
    def __init__(self,name,age=21):
        self.name=name
        self.age=age

    def __str__(self):          #display in string
        return f"{self.name} {self.age}"

    def greet(self):
        print(f"hello {self.name}. how are you?")


p1=person("nabin")
print(p1)
# print(p1.age)
p1.greet()
