# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionary items are ordered, changeable, and do not allow duplicates.
# Dictionary items are ordered, changeable, and do not allow duplicates.


# learning about dictionary
print("\n\ncreating dictionary:")
mydict={
    "name":"nabin basent",
    "age":20,
    "address":"belbari",
    "year":2025,
    "color":["red","blue","green"]

}

print(mydict)
print(len(mydict))
print(type(mydict))

dictconstruct=dict(name="nabin",age=20,address="belbari")
print(dictconstruct)

# accesssing dictonary items
print("\n\naccessing dictonary itrms:")
print(mydict["name"])           #getting the value of item using key name
print(mydict.keys())            #getting all the key name in dictonary
print(mydict.values())          #getting the values in dictonary
print(mydict.items())           #get the list of items in key values pairs

# checking the item if exist in dictonary using key 
if "name" in mydict:
    print("yes it in dict")

# changing items in dictonary
print("\n\nchanging items in dictonary:")
mydict["year"]=2014
print(mydict)
mydict.update({"year":2005})
print(mydict)

# adding items in dictonary
print("\n\nadding new items in dictonary:")
mydict["target"]="learning"         #adding new items
print(mydict)
mydict.update({"aim":"money"})
print(mydict)

# removing items
print("\n\nremoving item:")
mydict.pop("aim")           #this emove items using key 
print(mydict)
mydict.popitem()            #remove last items in dictonary
print(mydict)
# del mydict()  this delets the whole dictonary
# print(mydict)
# mydict.clear()              #remove all the items in dictonarty
print(mydict)

# looping dictonary
print("\n\nlooping the items in dictonary:")
for x in mydict:
    print(mydict[x])
    print(x)


#copying dictonary
print("\n\ncopying dictonary:")
mynew=mydict.copy()
print(mynew)

#nested dictonary
print("\n\nnested dictonary:")
nested={
    "child1":{
        "name":"nabin",
        "age":20
    },
    "child2":{
        "name":"nishan",
        "age":23
    },
    "child3":{
        "name":"nischal",
        "age":19
    }
}
print(nested)
for x in nested:
    print(nested[x])

print(nested["child1"])