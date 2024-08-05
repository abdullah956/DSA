class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0,head)
        prev , current = dummy , head
        while current and current.next :
            #saving ptrs 
            nextPair = current.next.next
            second = current.next
            
            #reverse pair 
            second.next = current
            current.next = nextPair
            prev.next = second
            
            #updating ptrs 
            prev = current 
            current = nextPair
        return dummy.next