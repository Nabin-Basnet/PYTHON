# # Inheritance allows us to define a class that inherits all the 
# # methods and properties from another class.

# class person:
#     def __init__(self,name,age,address):
#         self.name=name
#         self.age=age
#         self.address=address

#     def detail(self):
#         print(f"hello every my name is {self.name} . i am {self.age} years old. and i live in {self.address}")



# x=person("nabin",20,"dulari")
# x.detail()

# # here we create the class name students inherating the property of person

# class students(person):
#     def intro(self):
#         print(f"my name is {self.name} . i am {self.age} years old.i live in {self.address}")

# y=students("nishan",23,"laxmimargha")
# y.intro()


class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def fun():
        print("hello")

class student(person):
    def __init__(self,name,age,roll):
        super().__init__(name,age)
        self.roll=roll

    def __str__(self):
        return f"{self.name},{self.age},{self.roll}"
    
    # def fun(self):
    #     print("hello")


# p1=person("nabin",20)
# print(p1)
# print(p1.age)
# p1.greet()
s1=student.fun()
print(s1)

# s1.fun()