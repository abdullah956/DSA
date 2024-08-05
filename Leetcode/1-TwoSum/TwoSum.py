from typing import List


class Solution:
    def twoSum(self, nums, target) -> List:
        checklist = dict()
        for i in range(len(nums)):
            num = nums[i]
            checklistnumber = target - num
            if num in checklist :
                return [checklist[num],i]
            else :
                checklist[checklistnumber]=i
                
s = Solution()
array = [2,7,11,15]
target = 9
array2 = s.twoSum(array,target)
print(array2)