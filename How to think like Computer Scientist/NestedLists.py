### Nested Lists ###
''' A nested list is a list that appears as an element in another list. '''

nested = ["hello", 2.0, 5, [10, 20]]
innerlist = nested[3]
print(innerlist)
item = innerlist[1]
print(item)

print(nested[3][1])

''' To extract an element from the nested list, we can proceed in two steps.
    First, extract the nested list, then extract the item of interest.
    It is also possible to combine those steps using bracket operators that
    evaluate from left to right. '''


