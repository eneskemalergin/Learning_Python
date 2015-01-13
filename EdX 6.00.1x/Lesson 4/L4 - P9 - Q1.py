## L4 - P9 - Q1

'''
 Write a Python function, odd, that takes in one number and returns True
 when the number is odd and False otherwise.

You should use the % (mod) operator, not if.
'''

def odd(x):
    return(x % 2 == 1)

# With use of if else:
def odd(x):
    if x % 2 == 1:
        return(True)
    else:
        return(False)
