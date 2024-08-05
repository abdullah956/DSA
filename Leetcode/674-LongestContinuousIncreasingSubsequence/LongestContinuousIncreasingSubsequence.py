from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result=0
        anchor=0
        for i in range(len(nums)) :
            if i>0 and nums[i-1]>=nums[i] :
                anchor = i
            result=max(result,i-anchor+1)
        return result

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        currentlongest = 1
        alltimelongest = 1
        for i in range(len(nums)-1) :
            if nums[i] < nums[i+1] :
                currentlongest+=1
            else:
                currentlongest=1
            alltimelongest=max(currentlongest,alltimelongest)
        return alltimelongest