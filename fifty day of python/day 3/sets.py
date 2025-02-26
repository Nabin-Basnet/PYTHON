# learning about the sets
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
#  Set items are unchangeable, but you can remove items and add new items.
#  Sets are unordered, so you cannot be sure in which order the items will appear.
# Sets cannot have two items with the same value.

print("\n\ncreating sets:")
sett={"nabin","smriti","nishan","nischal"}
print(sett)

# we cannot accsess items in array using index
# pint(sett[8])
# but we can loop through set items

print("\n\naccessing the set items:")
for x in sett:
    print(x)

# checking the items in sets
print("\n\nchecking is items in set")
print("banana" in sett)
print("nabin" in sett)
print("banana" not in sett)

# addind set items 
print("\n\nadding items in sets:")
sett.add("hari")
print(sett)

# adding items from another sets in current set
sets={"prapti","karuna","nita"}
sets.update(sett)
print(sets)

# removing items in set 
print("\n\nremoving items from set:")
sett.remove("nischal")
print(sett)
sett.discard("hari")
print(sett)

# loop items
print("\n\nlooping the set items:")
for x in sett:
    print(x)
    