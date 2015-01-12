# Counting Bobs
# Author: Enes Kemal Ergin
'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''
s = 'azcbobobegghakl'
count = 0
for i in xrange(len(s)):
    if s[i:].startswith("bob"):
        count += 1
print("Number of times bob occurs is: " + str(count))