# -*- coding: cp1252 -*-
''' Find Function '''
#In a sense, find is the opposite of the indexing operator. 
def find(astring, achar):
    """
    Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring.
    """
    ix = 0
    found = False
    while ix < len(astring) and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return -1

print(find("Compsci", "p"))
print(find("Compsci", "C"))
print(find("Compsci", "i"))
print(find("Compsci", "x"))

# Lets modify the function above.
'''adding a third parameter for the starting position in the search string: '''
def find2(astring, achar, start):
    """
    Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring.
    """
    ix = start
    found = False
    while ix < len(astring) and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return -1

print(find2('banana', 'a', 2))
#--------------------------------------------------------------------------------#
'''Better still, we can combine find and find2 using an optional parameter.'''
def find3(astring, achar, start=0):
    """
    Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring.
    """
    ix = start
    found = False
    while ix < len(astring) and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return -1

print(find3('banana', 'a', 2))
#---------------------------------------------------------------------------------------#
'''Adding another optional parameter to find makes it search from a starting position,
up to but not including the end position.'''

def find4(astring, achar, start=0, end=None):
    """
    Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring.
    """
    ix = start
    if end == None:
        end = len(astring)

    found = False
    while ix < end and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return -1

ss = "Python strings have some interesting methods."

print(find4(ss, 's'))
print(find4(ss, 's', 7))
print(find4(ss, 's', 8))
print(find4(ss, 's', 8, 13))
print(find4(ss, '.'))

'''The optional value for end is interesting.
We give it a default value None if the caller does not supply any argument.
In the body of the function we test what end is
and if the caller did not supply any argument,
we reassign end to be the length of the string.
If the caller has supplied an argument for end,
however, the caller’s value will be used in the loop.
'''


















