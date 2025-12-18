# The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.
# This set of numbers has its own data type called range.

# range  can be create whith 1 2 or 3 arguments

x=range(10)   #creating an range of number upto 10
print(x)
print(list(x)) #convert to list to display the items


# range with two argument are use to indicate the starting and ending point of the range
a=range(3,15)
print(a)
print(list(a))


# If the range function is called with three arguments, the third argument represents the step value.
# The step value means the difference between each number in the sequence. It is optional, and if not provided, it defaults to 1.

b=range(3,20,2)
print(b)
print(list(b))

# range can also be used in for loop
for i in range(10):
    print(i)