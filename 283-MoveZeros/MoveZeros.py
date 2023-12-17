from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        w = 0
        for r in range(len(nums)) :
            if nums[r] !=0 :
                nums[w] = nums[r]
                w +=1
        print(w)
        while w<len(nums) :
            nums[w]=0
            w+=1
nums=[1,4,0,2,0,3]
s = Solution()
print(s.moveZeroes(nums))