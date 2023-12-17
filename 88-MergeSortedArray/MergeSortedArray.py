from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #for last index of nums1 making a pointer
        last = m+n-1
        
        #merge in reverse order 
        while m > 0 and n > 0 :
            if nums1[m-1] > nums2[n-1] :
                #coping the value at nums[m-1] to the last pointer
                nums1[last] = nums1[m-1]
                m-=1
            else :
                nums1[last] = nums2[n-1]
                n-=1
            last-=1
        
        #fill nums1 with leftover nums2 
        while n > 0 :
            nums1[last] = nums2[n-1]
            n-=1
            last-=1
        #for edge cases like what if we have nums2 remaining but nums1 ended (m=0) already
        #just add the remaining nums2 at first
        
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
s=Solution()
s.merge(nums1,len(nums1),nums2,len(nums2))