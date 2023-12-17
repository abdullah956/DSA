class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        slow, fast, start = head, head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while start != slow:
                    slow = slow.next
                    start = start.next
                return start
            
        return None