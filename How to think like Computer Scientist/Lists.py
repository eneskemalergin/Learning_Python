### LISTS ###

''' A list is a sequential collection of Python data values,
    where each value is identified by an index.
    The values that make up a list are called its elements
'''

# Enclosing the elements with brackets is the easiest way to create a list

[10,20,30,40] # Example of list contains integers

["spam","bungee","swallow"] # Example of list contains strings

["hello", 2.0, 5, [10, 20]] # Lists with another list/lists in it called nested lists...

''' Empty list denoted with [] '''

vocabulary = ["iteration", "selection", "control"]
numbers = [17, 123]
empty = []
mixedlist = ["hello", 2.0, 5*2, [10, 20]]

print(numbers)
print(mixedlist)
newlist = [ numbers, vocabulary ]
print(newlist)

## List Length ##

''' The function that we've used for strings "len" is working here as well.
    It returns the length of the list
'''

# Important: len only returns the top-most length, sublists are considered to be single item...
alist =  ["hello", 2.0, 5, [10, 20]]
print(len(alist))
print(len(['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]))

## Accessing Elements ##

''' The syntax for accessing the elements of a list is the same as
    the syntax for accessing the characters of a string.
'''
numbers = [17, 123, 87, 34, 66, 8398, 44]
print(numbers[2])
print(numbers[9 - 8])
print(numbers[-2])
print(numbers[len(numbers) - 1])

# Question:
alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
print(alist[2][0])

## List Membership ##

''' in and not in are boolean operators that test membership in a sequence.
    We used them previously with strings and they also work here.
'''

fruit = ["apple", "orange", "banana", "cherry"]

print("apple" in fruit)
print("pear" in fruit)


