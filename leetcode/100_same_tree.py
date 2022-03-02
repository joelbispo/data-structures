#same tree

class Solution:
    def isSameTree(self, p, q):
        #base-cases
        if not p and not q:
            return True
        if not p or not q:
            return False
        if q.val != p.val:
            return False
         #if they are the same, I keep searching   
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right))
