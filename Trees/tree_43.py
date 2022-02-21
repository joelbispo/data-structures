# Question 4.3 
# Given a sorted (increasing order) array, write an algorithm to create a binary tree with 
# minimal height


class Node:
    def __init__(self, value = None):
        self.left = None
        self.right = None
        self.value = value if value else None

    def insert(self, value):

        #check if the value of the node exist
        if self.value is None:
            #inserting into the left node
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            #inserting into the right node
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)                    
        else:
            self.value = value
    
    def add_to_tree(self, arr, start, end):
        if end < start:
            return None
        mid = (start+end)/2
       
        #insert the midle of the array
        node = Node(arr[mid])
        node.left = self.add_to_tree(arr, start, mid-1)
        node.ritht = self.add_to_tree(arr, mid+1, end)

        return node

    def create_minimal_bst(self, arr):
        return self.add_to_tree(arr, 0, len(arr)-1)

