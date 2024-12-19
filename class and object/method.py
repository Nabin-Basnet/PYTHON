class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfun(self):
        print("hello")

    def __str__(self):
        return f"{self.name} {self.age}"

p1=person("nabin",20)
print(f"my name is {p1.name} and i am {p1.age}")


print(p1)
p1.myfun()