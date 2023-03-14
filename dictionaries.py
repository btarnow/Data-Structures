# CODEWARS: ISOGRAMS
# https://www.codewars.com/kata/54ba84be607a92aa900000f1 

# An isogram is a word that has no repeating letters, consecutive or 
# non-consecutive. Implement a function that determines whether a string that 
# contains only letters is an isogram. Assume the empty string is an isogram. 
# Ignore letter case.

def is_isogram(string):

    letter_freq = {}
    
    for char in string.lower(): 
        letter_freq[char] = letter_freq.get(char, 0) + 1 

    for value in letter_freq.values():
        if value > 1:
            return False

    return True 

print(is_isogram("aba"))

