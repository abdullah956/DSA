class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0,head) #dummynode
        prev , current = head , head.next #previous is head and current is ahead of prev
        while current :
            if current.val >= prev.val : #already in order no need to sort
                prev , current = current , current.next #update the pointers
                continue #to the next iteration
            insert = dummy #insert will tell we have tp add our node 
            while current.val > insert.next.val : #to find insertion spot
                insert = insert.next
            prev.next = current.next #point prev to next node of current
            current.next = insert.next #current joining to insert next node
            insert.next = current #insert node connecting to current
            current = prev.next # we have current.next the next nod ein prev.next
        return dummy.next
#w dont hae to updateprevious bcz it will come to place before current after every ieration