# Class: A blueprint for creating objects. It defines the structure and behavior
#  (attributes and methods) that the objects created from it will have.
#  &
# Object: An instance of a class. It represents a specific entity with the
#  attributes and behaviors defined by its class.

class person:
    name="nabin"
    occupation="student"
    age=20
    def info(self):
        print(f"{self.name} is a {self.occupation} at the age of {self.age}.")

a =person()
print(a.info())


    