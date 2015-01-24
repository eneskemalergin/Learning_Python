## L5 - P5 - Q1

''' Write greatest common divisor algorithm using recursion '''


def gcdRecur(a, b):

    # Base case is when b = 0
    if b == 0:
        return a

    # Recursive case
    return gcdRecur(b, a % b)
