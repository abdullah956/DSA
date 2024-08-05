class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head :
            return None
        length , tail = 1 , head
        #taking length and finding tail
        while tail.next :
            tail = tail.next
            length+=1
        #rotations
        k = k % length
        if k == 0 :
            return head
        #rotating
        current = head
        for i in range(length - k - 1) :
            current = current.next
        #conecting tail to head
        tail.next = head 
        #making new head
        head = current.next
        #last node next pointing to null
        current.next = None
        return head
        