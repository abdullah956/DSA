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