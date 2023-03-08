
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



    
