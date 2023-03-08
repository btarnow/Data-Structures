from collections import deque

# A queue --> first in, first out 
class Queue:
    
    def __init__(self):
        self.data = []


    def enqueue(self, item):
        """Add item to the queue"""

        self.data.append(item)

    
    def dequeue(self):
        """Remove and return first item in queue."""

        if self.is_empty():
            return None
        return self.data.pop(0)
    
    
    def is_empty(self):
        """Returns True if queue is empty"""

        return self.data == []
    

class BetterQueue:
    def __init__(self):
        self.data = deque()

    
    def enqueue(self, item):
        
        self.data.append(item)


    def dequeue(self):
        if self.is_empty():
            return None 
        return self.data.popleft()
    
    def is_empty(self):
        if self.data:
            return False 
        else:
            return True



class Node: 

    def __ini__(self, data):
        self.data = data
        self.next = None
    
# Write a function that takes in the head node of a linked list and prints the
# data of every node in the list 

def print_nodes(head):

    current = head 

    while current: 
        print(current.data)
        current = current.next 


# Print Odd Nodes 

# create a method that takes in self 

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def print_odd_nodes(self):
        
        loop_counter = 0 

        current= self.head 

        while current: 
            if loop_counter % 2 != 0:
                print(current.data)
            current = current.next
            loop_counter += 1
        
# Write a method for this class called append. It should take in a node instance
# and add it to the end of the linked list. Remember to account for appending 
# to an empty list. 

# reassign the node instance to be the tail 

    def append(self, node):
        if self.tail == None: 
            self.tail = node 
        else: 
            self.tail = node

# Remove by value
# Write a function that removes a node with a given value from a singly-linked list.
# It should return the head node. The function should take in two arguments-- head and value

# establish a current node as the head 

# iterate through the linked list to see if any of the node's data matches the given value 
    # if/when you find the node with the value, remove it 


# return the head 

def remove_node(head, value):

    current = head 

    while current: 
        if current.next.data == value: 
            current.next = current.next.next 
            break 

        current = current.next 

    return head 
