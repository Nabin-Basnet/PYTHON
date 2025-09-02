#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
fruits=["apple","banana","mango","orange"]
for x in fruits:
    print(x)

# looping the string
for x in "banana":
    print(x)

#break sataement in for loop
for x in fruits:
    print(x)
    if x=="mango":
        break


# using range function
for x in range(1,11):
    print(x)