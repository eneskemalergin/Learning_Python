## L5 - P4 - Q1

''' Write a greatest common divisor algorithm '''
def gcdIter(a, b):
    while(b != 0):
        remainder = a % b
        a = b
        b = remainder
    return a    
