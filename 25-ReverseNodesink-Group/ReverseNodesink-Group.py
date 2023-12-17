class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0,head)
        groupprev = dummy # for last memeber of prev group 
        while True :
            kth = self.getKth(groupprev , k)
            if not kth :
                break
            groupnext = kth.next #first member of next group
            
            #reverse
            prev, current=kth.next,groupprev.next
            while current != groupnext:
                Next  = current.next
                current.next = prev
                prev = current
                current = Next
            
            temp = groupprev.next #temp golding start of group
            groupprev.next = kth #GP.N holds the last elemtn
            groupprev = temp 
        return dummy.next
            
            
    def getKth(self,current : ListNode,k : int) -> ListNode : # to get the last kth node
        while current and k > 0 :
            current=current.next
            k-=1
        return current