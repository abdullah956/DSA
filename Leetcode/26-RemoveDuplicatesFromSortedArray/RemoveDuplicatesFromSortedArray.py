import typing
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow_pointer= 1
        if len(nums)<1 :
            return 0
        for fast_pointer in range(slow_pointer,len(nums)) :
            if nums[fast_pointer] != nums[fast_pointer-1] :
                nums[slow_pointer] = nums[fast_pointer]
                slow_pointer = slow_pointer +1
        return slow_pointer
s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))