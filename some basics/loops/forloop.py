# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
fruits=["apple","mango","banana","orange","papaya","guava","watermelon"]
status=["--------------ready to eat-------","---------------not ready to harvest at-------------"]

for f in fruits:  #for loop dont required any index 
    print(f)
    if f=="orange":  #With the break statement we can stop the loop before it has looped through all the items:
        break   #break statement break the loop in certain condition

#looping through the string
name="nabin basnet"

for n in name:
    print(n)

#print the number upto 6
for x in range(6):
    print(x)
#print the numbers from 3 to 10
for y in range(3,10):
    print(y)
#print the all fruits 
for f in fruits:
    print(f)
else:             #The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
    print("all fruits are printeed")


#nested loop(loop inside the loop)
for s in status:
    print(s)
    for f in fruits:
        print(f)