class Solution :
    def isPalindrome(self, head) -> bool :
        nums = []
        while head :
            nums.append(head.val)
            head = head.next
        l=0
        r=len(nums)-1
        while l<=r :
            if nums[l]!=nums[r]:
                return False
            l+=1
            r-=1
        return True;