# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.


# creating tuple
tuplee=("apple","ball","cat","dog","egg","fish")
print(len(tuplee))
print(tuplee)
print(type(tuplee))

# tuple storing number
tuplenum=(2,5,7,9,0)
print(tuplenum)

# It is also possible to use the tuple() constructor to make a tuple.
tupleCon=tuple(("apple",1,5,8,"mango"))
print(tupleCon)
print("hello every one\
 we are learning about tuple here")

# accessing tuple
print("\n\naccessing tuple:")
print(tuplee[1])                #accessing tuple using index we can also use negative index
#we can also use range of index to access as like in list

# check if items exists
print("\n\nchecking existance of items in tuple:")
if "apple" in tuplee:
    print("yes it is in tuple name tuplee")

# update tuple
"""we cannot drectly change tuple it is unchangable also called immutable
but for updating or changing item in tuple we can convert tuple into list 
 change the or update list and again convert back to tuple
 """
print("\n\nupdating tuple indirectly:")
x=list(tuplee)
x[1]="red"
y=tuple(x)
print(y)
# we can use same method for updating using different methods


#looping tuple
print("\n\nlooping the tuples:")
for i in tuplee:
    print(i)


print("\nusing range:")
for i in range(len(tuplee)):
    print(tuplee[i])

print("\n\nusing while loop:")
while i < len(tuplee):
    print(tuplee[i])
    i=i+1

print(tuplee)

# joining tuple
print("\n\njoining tuple")
newtuple=tuplee+tuplenum
print(newtuple)
# print(newtuple.short())