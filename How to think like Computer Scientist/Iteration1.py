''' The For loop again '''

for f in ["Enes", "Aiykerim", "Sherzat", "Alisher", "Nurbek", "Mederbek", "Zhanarzhan"]:
    print "Hi", f, "Please come to my party on Saturday"

print "----------------------------------------------"
def sumTo(aBound):
    theSum = 0
    for aNumber in range(1, aBound + 1):
        theSum = theSum + aNumber

    return theSum

print(sumTo(4))

print(sumTo(1000))


''' The While Loop '''

# This is another kind of looping statement in python
# Similar to if statement, while loop uses a boolean expression to control the flow of execution
# Statements in the body will execute until expression evaluates False

print "-----------------------------------------------------"
def sumTo(aBound):
    """ Return the sum of 1+2+3 ... n """

    theSum  = 0
    aNumber = 1
    while aNumber <= aBound:
        theSum = theSum + aNumber
        aNumber = aNumber + 1
    return theSum

print(sumTo(4))

print(sumTo(1000))


# ''' Infinite loop '''
'''
n = 10
answer = 1
while n > 0:
    answer = answer + n
    n = n + 1
print(answer)

'''
def newtonSqrt(n, howmany):
    approx = 0.5 * n
    for i in range(howmany):
        betterapprox = 0.5 * (approx + n/approx)
        approx = betterapprox
    return betterapprox

print(newtonSqrt(10, 3))
print(newtonSqrt(10, 5))
print(newtonSqrt(10, 10))

print "##############################################################"

print("n", '\t', "2**n")     #table column headings
print("---", '\t', "-----")

for x in range(13):        # generate values for columns
    print(x, '\t', 2 ** x)
