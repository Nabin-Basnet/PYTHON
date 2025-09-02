class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def persondetails(self):
        print(f"my name is {self.name} and i am {self.age}")

class student(person):
    def __init__(self,name,age,year):
        # person.__init__(self,name,age)
        super().__init__(name,age)
        self.graduationyear=year
    def studentinfo(self):
        print("this is inherated from class name person")
        print("Hello friends i am ",self.name," . i am ",self.age," and iam gradauataed in the year ",self.graduationyear)




x=person("nabin",20)
x.persondetails()


s=student("ram" ,29,2019)
s.studentinfo()
