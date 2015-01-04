### List Continues ###

## Concatenation and Repetition ##
''' Again, as with strings, the + operator concatenaties lists. Similarly, the * operator repeats
    the items in a list a given number of times.
'''
fruit = ["apple", "orange", "banana", "cherry"]
print([1, 2] + [3, 4])
print(fruit + [6, 7, 8, 9])

print([0] * 4)
print([1, 2, ["hello", "goodbye"]] * 2)

# Question 1
alist = [1, 3, 5]
blist = [2, 4, 6]
print(alist + blist)
''' [1, 3, 5, 2, 4, 6] '''

# Question 2
alist = [1, 3, 5]
print(alist * 3)
''' [1, 3, 5, 1, 3, 5, 1, 3, 5] '''


## List Slices ##
''' The slice operation we saw with strings also work on lists. '''
a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list[1:3])
print(a_list[:4])
print(a_list[3:])
print(a_list[:])

## List are Mutable ##
''' Unlike strings, lists are mutable. '''
''' Using the indexing operator (square brackets) on the left side
    of an assignment, we can update one of the list items. '''
 
fruit = ["banana", "apple", "cherry"]
print(fruit)

fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)

''' By combining assignment with the slice operator we can update several elements at once. '''


alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y']
print(alist)


''' We can also remove elements from a list by assigning the empty list to them.'''

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = []
print(alist)


''' We can even insert elements into a list by squeezing them into an empty
    slice at the desired location.'''

alist = ['a', 'd', 'f']
alist[1:1] = ['b', 'c']
print(alist)
alist[4:4] = ['e']
print(alist)

## List Deletion ##
''' Using slices to delete list elements can be awkward and therefore error-prone. '''
''' The del statement removes an element from a list by using its position. '''

a = ['one', 'two', 'three']
del a[1]
print(a)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:5]
print(alist)

## Cloning Lists ##

''' If we want to modify a list and also keep a copy of the original,
we need to be able to make a copy of the list itself, not just the reference.
This process is sometimes called cloning, to avoid the ambiguity of the word copy.'''

''' The easiest way to clone a list is to use the slice operator. '''
a = [81, 82, 83]
b = a[:]
print a == b

## Repetition and References ##
origlist = [45, 76, 34, 55]
print(origlist * 3)
''' [45, 76, 34, 55, 45, 76, 34, 55, 45, 76, 34, 55] '''

newlist = [origlist] * 3

print(newlist)

