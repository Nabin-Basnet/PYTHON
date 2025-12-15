#list are data type which is used to store multiple data in single variable like in arrey

fruits=['apple','banana', 'orange' ,'papaya']
print(fruits)

# List items are ordered, changeable, and allow duplicate values.
lists=["apple",24,32,"mango"]  #creation of list
lists[2]=49 #replace the item at the index
lists.append(34)  #add an item at last of the list
lists.insert(2,"orange") #add item at any index
lists.pop(1)  #remove an item at the given index
lists.remove("mango")  #remove the items by it name
print(lists)



#looping the list item
for x in lists:
    print(x)



lists.clear()   #clear the all item in the list
print(lists)