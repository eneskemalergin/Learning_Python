### List Methods ###

mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12)
print(mylist)
print(mylist.count(12))

print(mylist.index(3))
print(mylist.count(5))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem = mylist.pop()
print(lastitem)
print(mylist)

''' Method 	Parameters 	Result 	        Description
    append 	item 	        mutator 	Adds a new item to the end of a list
    insert 	position, item 	mutator 	Inserts a new item at the position given
    pop 	none 	        hybrid 	        Removes and returns the last item
    pop 	position 	hybrid 	        Removes and returns the item at position
    sort 	none 	        mutator 	Modifies a list to be sorted
    reverse 	none 	        mutator 	Modifies a list to be in reverse order
    index 	item 	        return idx 	Returns the position of first occurrence of item
    count 	item 	        return ct 	Returns the number of occurrences of item
    remove 	item 	        mutator 	Removes the first occurrence of item
'''

mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist = mylist.sort()   #probably an error
print(mylist)
