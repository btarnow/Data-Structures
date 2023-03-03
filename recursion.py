# PROBLEM 1:
# Write a function that returns the length of a list using recursion

def list_length(lst):
    if not lst:
        return 0 
    else: 
        return 1 + list_length(lst[1:])
    

# PROBLEM 2: 
# Write a recursive function that prints the numbers 1-5 

# create a function that takes in a variable set to n=1 
# if n is less than 5, print n 
# call it again but add 1 to n 

def count_recursively(n=1):

    # this is the base case here. Once this is true, it will 
    while n > 5:
        return
    
    print(n)
    count_recursively(n+1)


# PROBLEM 3: 
# Write a recursive function that will take a list of numbers, and
# returns the largest number in the list 

def find_largest_num(lst, largest_num=None):

    if not lst:
        return largest_num
    if largest_num is None or lst[0] > largest_num:
        largest_num =  lst[0]
    return find_largest_num(lst[1:], largest_num)


# PROBLEM 4:
# Write a recursive function that takes in a list of numbers and returns a list 
# where all of the numbers are doubled. 

def double_nums(nums, doubled_list = []):
	
	if not nums:
		return doubled_list
	
	doubled_list.append(nums[0] * 2)
	
	return double_nums(nums[1:], doubled_list)

# PROBLEM 5: 
# Write a recursive function that will take in a string and reverse it and return
# the reversed string. 

# input --> "apple"
# output --> "elppa"

# base case --> taking the original string and removing characters and then when 
# the string is empty, it can stop 

def reverse_str(str, reversed_str=""):
     
     if str == "":
          return reversed_str 
     
     reversed_str = str[0] + reversed_str

     return reverse_str(str[1:], reversed_str)

# ANOTHER solution to the problem above: 

# def reverse_str(s):
    # if not str:
    #      return str

    # return reverse_str(str[1:]) + s[0]) 

