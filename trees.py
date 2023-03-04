"""Practice with the tree data structure"""

# ----- Review Notes ----- #
    # Every linked list is a tree, but not every tree is a linked list.

    # Tree nodes have data and children 

    # SAMPLE TREE CREATION: 
    # morgan = Node("Morgan", [])
    # morgan.children.append(Node("Taylor", []))
    # morgan.children.append(Node("Marcus", []))
    # morgan.children --> [<Node Taylor>, <Node Marcus>]
    # OR you could create the child node first and then append that variable name
    # dave = Node("Dave", [])
    # morgan.children.append(dave)



class Node: 
    """Node in a tree"""

    def __init__(self, data, children):
        self.data = data
        self.children = children 
    
    def __repr__(self):
        """Reader-friendly representation"""

        return f"<Node {self.data}>"
    
    def find_node(self, data)


# ----- TREE PROBLEMS ----- #

# PROBLEM 1: 
# Given a tree node class, write a method that returns the number of nodes 
# in the tree 

# Pseudocode: 
    # create a method called count_nodes that takes in the argument of a tree's 
    # root (self)

    # create a variable called node_count and set it to zero

    # go through every node in the tree, incrementing the count of node_count 
    # by 1 for each node visited

    # return the node count 

    def count_nodes(self):
        node_count = 0 

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()
            node_count += 1 
            to_visit.extend(current.children)
        
        return node_count 


# PROBLEM 2: 
# Given a tree Node class, write a method that takes an item as its only 
# parameter and returns True if the data for any node in the tree matches the 
# given item. Otherwise, it should return False.

# Pseudocode: 
    # create a method called is_item_in_tree that takes in an item as a parameter 

    # create a list of nodes to visit, starting at the root (self)
    
    # iterate through the to visit list, setting a variable called current to 
    # a node popped from the to visit list 
        # if that current node's data matches the item, return true
        # else, add that nodes children to the to_visit list and continue 

    # if there are no more nodes to visit and none of the previously checked 
    # node's data matched the item's, return false 


def is_item_in_tree(self, item):

    to_visit = [self]

    while to_visit:
        current = to_visit.pop()

        if current.data == item:
            return True
        
        to_visit.extend(current.children)
    
    return False 


# PROBLEM 3: 
# Given a tree Node class, write a method that takes an item as its only 
# parameter and returns the highest ranking node whose data matches the given 
# item. (If there are no matching nodes, it should return None).

# Pseudocode: 
    # create a method called find_highest_ranking_node that takes in an item 

    # This will need to be a breadth first search so that the highest matching 
    # node is found 

    # 





