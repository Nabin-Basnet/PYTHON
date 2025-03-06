# Inheritance allows us to define a class that inherits all the 
# methods and properties from another class.

class person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def detail(self):
        print(f"hello every my name is {self.name} . i am {self.age} years old. and i live in {self.address}")



x=person("nabin",20,"dulari")
x.detail()

# here we create the class name students inherating the property of person

class students(person):
    def intro(self):
        print(f"my name is {self.name} . i am {self.age} years old.i live in {self.address}")

y=students("nishan",23,"laxmimargha")
y.intro()

