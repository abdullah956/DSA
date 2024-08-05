import typing
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        actualsize = 0
        if not nums:
            return 0
        for i in range(len(nums)) :
            if nums[i]!= val :
                nums[actualsize] = nums[i]
                actualsize = actualsize + 1
        return actualsize
nums = [3,2,2,3]
s = Solution()
print(s.removeElement(nums,3))