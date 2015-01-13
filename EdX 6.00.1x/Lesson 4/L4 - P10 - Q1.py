## L4 - P10 - Q1

'''
Define a function isVowel(char) that returns True if char is a vowel
('a', 'e', 'i', 'o', or 'u'), and False otherwise. You can assume that
char is a single letter of any case (ie, 'A' and 'a' are both valid).

Do not use the keyword in. Your function should take in a
single string and return a boolean.
'''
def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return True
    elif char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        return True
    else:
        return False
