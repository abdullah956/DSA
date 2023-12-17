
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left , right = ListNode() , ListNode()
        ltail , rtail = left , right
        current = head
        while current :
            if current.val < x :
                ltail.next = current
                ltail = ltail.next
            else :
                rtail.next = current 
                rtail = rtail.next
            current = current.next
        ltail.next = right.next
        rtail.next = None
        return left.next