## L3 - P2 - Q3

'''Write a while loop that sums the values 1 through end,
inclusive. end is a variable that we define for you. So,
for example, if we define end to be 6, your code should print out the result:

21

which is 1 + 2 + 3 + 4 + 5 + 6.

For problems such as these, do not include raw_input
statements or define the variable end. Our automating
testing will provide a value of end for you - so write
your code in the following box assuming end is already defined.

'''
end = 6
total = 0
num = 1
while num <= end:
    total += num
    num += 1


print(total)
