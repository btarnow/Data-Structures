
# TWO SUMS PROBLEM: 

def two_sums(nums, target):
    """Given a target number, this function returns the two indices thats values 
    add to the target"""


    visited = {}

    for index, num in enumerate(nums): 
        diff = target - num 
        if diff in visited: 
            return [visited[diff], index]
        visited[num] = index

print(two_sums([2, 1, 5, 3], 4))


# FIND MISSING WORDS: 
# https://drive.google.com/file/d/1F_fYYfDXH8i1A5TCRJS0D1gUKsHtGtA4/view 

def find_missing_words(s, t):
	list_s = s.split(" ")
	list_t = t.split(" ") 
	
	missing_words = []

	for word in list_s: 
		if word not in list_t:
			missing_words.append(word)

	return missing_words 

print(find_missing_words("I am using HackerRank to improve programming", "am HackerRank to improve"))


# CODEWARS: ISOGRAMS
# https://www.codewars.com/kata/54ba84be607a92aa900000f1 

# An isogram is a word that has no repeating letters, consecutive or 
# non-consecutive. Implement a function that determines whether a string that 
# contains only letters is an isogram. Assume the empty string is an isogram. 
# Ignore letter case.
def is_isogram(string):
    string = string.lower()

    for char in string: 
        # check each letter in the string. If any of the letters exist more than 
        # once, return false immediately 
        if string.count(char) > 1: 
            return False 
    return True 

print(is_isogram("abcEe"))