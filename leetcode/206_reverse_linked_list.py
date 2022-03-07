class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def reverseListRecursive(self, head):
        if not head or not head.next:
            return None
        reversedListHead = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return reversedListHead

        

        
