class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        prev = dummy
        slow , fast = head , head
        prev.next = slow
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return dummy.next
    
"""
    1<--2---3---4
    temp 3
    prev 2
    current.next 1
    current 3
    while current :
                temp  = current.next // for saving the next pointer reference before changing current
                current.next = prev // for reversing
                prev = current //updating the current
                current = temp // updating the current
"""