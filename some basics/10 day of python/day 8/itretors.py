# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you
#  can traverse through all the values.

my_tuple=("nabin","nishan","nischal","mohit")

itr=iter(my_tuple)
a=len(my_tuple)

for num in range(a):
    print(next(itr))

# print(next(itr))


# creating iterator 
# To create an object/class as an iterator you have to implement the
#  methods __iter__() and __next__() to your object.
# As you have learned in the Python Classes/Objects chapter, all classes
#  have a function called __init__(), which allows you to do some 
# initializing when the object is being created.
# The __iter__() method acts similar, you can do operations
#  (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must
#  return the next item in the sequence

class my_number:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        x=self.a
        self.a +=1
        return x
 

a=my_number()
another=iter(a)
for x in range(10):
    print(next(another))

# stopiteration
# The example above would continue forever if you had enough next() 
# statements, or if it was used in a for loop.
# To prevent the iteration from going on forever, we can use the 
# StopIteration statement.
# In the __next__() method, we can add a terminating condition to 
# raise an error if the iteration is done a specified number of times:

class num:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
        
classs=num()
itrate=iter(classs)
for x in itrate:
    print(x)
