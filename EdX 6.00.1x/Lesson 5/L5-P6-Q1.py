## L5 - P6 - Q1

''' Write an iterative function, lenIter, which computes the length of an input
argument (a string), by counting up the number of characters in the string.
'''

def lenIter(aStr):
    
    count = 0

    # Iterate over each character in the string, counting each one
    for char in aStr:
        count += 1
    return count
