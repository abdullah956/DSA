class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0,head)
        leftprev , current = dummy , head
        #reaching at position left
        for i in range (left-1) :
            leftprev = current
            current = current.next
        # current is on left leftprev is behind current
        # reverse  form left to right
        prev = None
        for i in range(right-left+1) :
            Next = current.next
            current.next = prev
            prev = current
            current = Next
        #updating the pointers
        leftprev.next.next = current #current node is after right
        leftprev.next = prev #prev is on right
        return dummy.next