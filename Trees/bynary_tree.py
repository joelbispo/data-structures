
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val
    
    def insert(self, value):
        #check if val is not None
        if self.value:
            #insert into the left
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            #insert into the right

            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)        
        else:
            self.value = value

    def print_tree(self):
        print(self.value)
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()
    
    def pre_order_traverse(self, node):
        res = []

        if node:
            res.append(node.value)
            res = res + self.pre_order_traverse(node.left)
            res = res + self.pre_order_traverse(node.right)
        return res
    
    
    def max_depth(self, root):
        if Node is None:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))



root = Node(20)

print(root.value)
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.print_tree()
print(root.pre_order_traverse(root))


    