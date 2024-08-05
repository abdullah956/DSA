from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma = nums[0]
        c = 0
        for n in nums :
            if c < 0 :
                c = 0 
            c += n
            ma = max(ma,c)
        return ma