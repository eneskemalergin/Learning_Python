# Counting Vowels
# Author: Enes Kemal Ergin
''' Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example,
if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
'''
s = 'azcbobobegghakl'
s_list = list(s) # Make a list with characters
count = 0
for i in s_list:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1
print("Number of vowels: " + str(count))