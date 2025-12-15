mydict={                         #creating the the dictionaries
    "name":"nabin",
    "address":"belbari",
    "age":20,
    "school":"itahari namuna"
}

print(mydict)     #access all data
print(mydict["address"])   #accessing the value using key 



mydict["name"]="sahabir"  #change the value
mydict.update({"age":21})   #update the dictionaries

mydict["father"]="myfather"  #add an item in dictionaries

mydict.pop("father")  #remove the items

for d in mydict:
    print(mydict[d])   #this print the value



for d in mydict:
    print(d)         #print the key 


for x, y in mydict.items():  #loop throw key value
    print(f"{x}: {y}")