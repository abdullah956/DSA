class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next : #not a node ora single node
            return head
        #spliting the list into two halfs
        left = head
        right = self.getMid(head) #fining the mid to split in half
        temp = right.next #saving right.next in a temp
        right.next = None #breaking the link in between 
        right = temp #then mving the right pointer 
        #recursion
        left = self.sortList(left)
        right = self.sortList(right)
        #return the lists after merging them
        return self.mergeLists(left,right)
        
    def getMid(self,head) :
        slow , fast = head , head.next
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def mergeLists(self,left,right) :
        dummy = ListNode()
        current = dummy
        while left and right :
            if left.val < right.val :
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current=current.next
        if left :
            current.next = left
        else:
            current.next = right
        return dummy.next