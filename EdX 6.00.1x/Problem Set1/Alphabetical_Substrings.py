# Alphabetical Substrings
# Author: Enes Kemal Ergin

'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters
occur in alphabetical order. For example, if s = 'azcbobobegghakl', 
then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print

Longest substring in alphabetical order is: abc
'''
s = 'azcbobobegghakl'
# s = "abcbcd"
pos = 0
maxLen = 0
startPos = 0
endPos = 0


def last_pos(pos):
    if pos < (len(s) - 1):
        if s[pos + 1] >= s[pos]:
            pos += 1
            if pos == len(s)-1:
                return len(s)
            else:
                return last_pos(pos)
        return pos


for i in range(len(s)):
    if last_pos(i) != None:
        diff = last_pos(i) - i+1
    if diff > maxLen:
        maxLen = diff
        startPos = i
        endPos = startPos + diff - 1

print(s[startPos:endPos+1])            