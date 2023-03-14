# CODEWARS: ISOGRAMS
# https://www.codewars.com/kata/54ba84be607a92aa900000f1 

# An isogram is a word that has no repeating letters, consecutive or 
# non-consecutive. Implement a function that determines whether a string that 
# contains only letters is an isogram. Assume the empty string is an isogram. 
# Ignore letter case.

# SOLUTION WITH A DICTIONARY: 
def is_isogram(string):

    letter_freq = {}
    
    for char in string.lower(): 
        letter_freq[char] = letter_freq.get(char, 0) + 1 

    for value in letter_freq.values():
        if value > 1:
            return False

    return True 

print(is_isogram("aba"))

#SOLUTION UTILIZING THE .COUNT METHOD IN PYTHON: 
def is_isogram_2(string):
    string = string.lower()

    for char in string: 
        # check each letter in the string. If any of the letters exist more than 
        # once, 
        if string.count(char) > 1: 
            return False 
    return True 

print(is_isogram_2("abcEe"))


