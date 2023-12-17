class Solution :
    def isPalindrome(self, head) -> bool :
        fast = head
        slow = head

        #find middle
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
        
        # reverse second half
        prev = None
        while slow :
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        #check palindrome
        left,right=head,prev 
        while right :
            if left.val != right.val :
                return False
            left = left.next
            right = right.next
        return True