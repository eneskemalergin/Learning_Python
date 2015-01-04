### List Comprehensions ###

''' An easy way to create a list from a sequence of values based on some selection criteria
    is to use a list comprehensions '''

''' [<expression> for <item> in <sequence> if  <condition>] '''

mylist = [1,2,3,4,5]

yourlist = [item ** 2 for item in mylist] # for iterates through each item in a sequence

print(yourlist)

''' To write the primes_upto function we will use the is_prime function to filter the sequence
    of integers coming from the range function. In other words,
    for every integer from 2 up to but not including n, if the integer is prime, keep it in the list.
'''
def primes_upto(n):
    """ Return a list of all prime numbers less than n using a list comprehension. """

    result = [num for num in range(2,n) if is_prime(num)]
    return result





