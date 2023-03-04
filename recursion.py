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



# PROBLEM 5: Write a function that takes in a list and returns a sum of all of 
# the numbers in a list using recursion 

# input --> [1, 2, 3, 4]
# output --> 10 

# Pseudocode: 
    # Base Case: When the starting list is empty. 

    # Create a variable set to none 

    # define a method that will take in a list. 

def sum_recursion(lst, sum_lst=0):
     
     if not lst: 
          return sum_lst 
     
     sum_lst += lst[0]

     return sum_recursion(lst[1:], sum_lst)


# PROBLEM 6: Write a function that computes the factorial of a number using 
# recursion. The factorial of a number n is defined as the product of all 
# numbers from 1 to n. For example, 4! = 4 x 3 x 2 x 1 = 24

# Base case: when n becomes 0 

def factorial_recursive(n):
     
    if n == 1:
        return 1
    return n * factorial_recursive(n-1)

# Output if n = 4: 
# 4
# 4*3
# 4*3*2
# 4*3*2*1

    