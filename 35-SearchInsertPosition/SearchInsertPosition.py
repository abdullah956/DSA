import typing
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right :
            mid = (left + right)//2
            if target == nums[mid] :
                return mid 
            if target>nums[mid] :
                left = mid +1
            else :
                right = mid -1
        return left

nums= [1,3,4,5]
s = Solution()
inp  = int(input("enter number you want to search"))
print(s.searchInsert(nums,inp))