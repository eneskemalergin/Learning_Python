### Tuples ###
## Tuples and Mutability ##

''' Strings:  Made up of characters
    Lists  :  Made up of elements of any type / it can be modified
    '''
# Strings are immutable , and lists are mutable.

''' A tuple, like a list, is a sequence of items of any type. Unlike lists,
    however, tuples are immutable. Syntactically, a tuple is a comma-separated sequence of values.
'''

# This example shows that tuples are not mutable
'''
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
julia[0] = 'X'
TypeError: 'tuple' object does not support item assignment

'''
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2])
print(julia[2:6])

print(len(julia))

julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)


tup = (5,)
print(type(tup))

x = (5)
print(type(x))

## Tuple Assignment ##

'''Python has a very powerful tuple assignment feature that allows a tuple
    of variables on the left of an assignment to be assigned values from a tuple
    on the right of the assignment.'''

temp = a
a = b
b = temp
# Equals
(a, b) = (b, a) # Using python tuples

''' Naturally, the number of variables on the left and the number of values on the right
have to be the same.

(a, b, c, d) = (1, 2, 3)
ValueError: need more than 3 values to unpack
'''

## Tuples as Return Values ##

def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return (c, a)

print(circleInfo(10))








