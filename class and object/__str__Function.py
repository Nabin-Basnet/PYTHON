# the __str__ method is a special method used to define how an object is represented
#  as a string. It is automatically called when you use the str() function or print 
# an object. This method is typically used to provide a user-friendly description
#  of the object.

class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name} {self.age}"

p1=person("nabin",20)
print(f"my name is {p1.name} and i am {p1.age}")


print(p1)