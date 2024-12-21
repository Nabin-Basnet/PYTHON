#Polymorphism is a concept in programming where a single function,
#  method, or object can behave differently based on the context in 
# which it is used. For example, a single function name can perform different 
# tasks depending on the type of input, or an object can take different forms
#  through inheritance. It helps make code more flexible and reusable by allowing
#  one interface to handle multiple underlying forms or data types.

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
