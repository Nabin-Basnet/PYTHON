listStr=["apple","mango","orange","banana"]
listNum=[1,2,3,4,8,9,0]
listNumStr=["apple",20,"orange",29,30,"banana"]


# printing the lists 
print("\n\n\nhere are the some lists:")
print(listStr)
print(listNum)
print(listNumStr)

# datatype of lists
print("\n\ndata type of list:")
print(type(listStr))
print(type(listNum))
print(type(listNumStr))

# using list construct to create list
Clist=list(("apple","ball","cat"))
print(Clist)

# accessing list
print("\n\n\naccessing lists:")
print(listStr[1])
print(listStr[-3])          #negative index means 
print(listStr[1:4])         #range of list
print(listStr[1:])          #display all the item in list after index 1
print(listStr[:3])          #display all item in list befor index 


# check if item in list
print("\n\nchecking is item in list:")
if "apple" in listStr:
    print("yes it in list")

# changing list items
print("\n\nchanging list items")
listStr[1]="ball"                   #replace the item of list in index 1
print(listStr)
# we can also chane the item from certain index 
# we can also replace 1 item by multiple items


# adding new item in list
print("\n\nadding items in list")
listStr.append("kera")      #add item at last of list
print(listStr)

#inserting items in certain index
listStr.insert(3,"guva")
print(listStr)

#murging two or append another list to certain list
print("\n\nlistStr after murging or appending listNum in it:")
listStr.extend(listNum)
print(listStr)

# removing items from list
print("\n\nremoving item from list")
listStr.remove("apple")             #remove item from list by item name
print(listStr)
listStr.pop(3)                      #remove items by it index
print(listStr)
listStr.pop()                       #remove list from last
print(listStr)
# del listStr                         #delete the complete list
# print(listStr)

# looping list
print("\ndisply all item sin list one by one:")
for x in listStr:       #list all item inlist on eby one
    print(x)
print("\ndisplay list by referring to their index")
for i in range(len(listStr)):
    print(listStr[i])


print("\nusing while loop")
i=0
while i < len(listStr):
    print(listStr[i])
    i+=1


#list comprehension
print("\n\nlist comprehension:")
oldlist=["apple","mango","banana"]
newlist=[]

for x in oldlist:
    if "a" in x:
        newlist.append(x)

print(newlist)


# sorting list
print("\nsorted list:")
oldlist.sort()
listNum.sort()
print(oldlist)
print(listNum)

print("\nsorting in discending order:")
listNum.sort(reverse=True)
print(listNum)

#copying list (creating list by copying another list)
print("\ncopying list:")
newnewlist=newlist.copy()
print(newnewlist)