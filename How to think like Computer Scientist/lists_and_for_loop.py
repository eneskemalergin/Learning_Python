### Lists and For Loop ###

''' It is also possible to perform list traversal using iteration by item as well
    as iteration by index '''

fruits = ["apple", "orange", "banana", "cherry"]

for afruit in fruits:     # by item
    print(afruit)

''' We can also use the indices to access the items in an iterative fashion.'''

fruits = ["apple", "orange", "banana", "cherry"]

for position in range(len(fruits)):     # by index
    print(fruits[position])


''' Any sequence expression can be used in a for loop. For example,
    the range function returns a sequence of integers. '''

for number in range(20):
    if number % 3 == 0:
        print(number)

numbers = [1, 2, 3, 4, 5]
print(numbers)

for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2

print(numbers)
