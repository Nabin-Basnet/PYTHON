#tuple is also a data type which is used to store the multiple values

tupels=("apple","banana","cat","dog","eagle")   #creating of tuple
print(tupels)  #display tuple
# tuple[2]="not work"  this doesnt work in tuple
#once the tupel is created it cannot be change it is  unchangeable, or immutable 
#to changge the tupel it should be converted into list and other operation are performed 

lists=list(tupels)  #tupel is converted to list
print(lists)
lists[2]="change"
lists.append("nabin")


t=tuple(lists) #now again tupel is converted into tuple

print(lists)
print(t)
print(tupels[2:])