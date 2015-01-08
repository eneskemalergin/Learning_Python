# Lecture2-Problem 11:
'''Assume that two variables, varA and varB, are assigned values, either numbers or strings.

Write a piece of Python code that prints out one of the following messages:

    "string involved" if either varA or varB are strings

    "bigger" if varA is larger than varB

    "equal" if varA is equal to varB

    "smaller" if varA is smaller than varB
'''
# Important Note: varA and varB will be provided by system
# My test cases:
# Test Case 1: varA = "Enes"; varB = "Kemal"
# Test Case 2: varA = "Enes"; varB = 1
# Test Case 3: varA = 2; varB = 1
# Test Case 4: varA = 1; varB = 1
# Test Case 5: varA = 1; varB = 2

varA = 1; varB = "Enes"
if type(varA) == str or type(varB) == str:
    print("string involved")
else:
    if varA > varB:
        print("bigger")
    elif varA == varB:
        print("equal")
    else:
        print("smaller")