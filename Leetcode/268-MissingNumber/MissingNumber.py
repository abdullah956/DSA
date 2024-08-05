from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i in range(len(nums)):
            result = result + (i-nums[i])
        return result


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Loop through numbers 0 to the last index of nums:
        #if the current iteration is not equal to the number (of our current index)
        #That is the missing number
        no_missing_num = 0 
        nums.sort() #First sort it so it is in order 
        for val in range(0, len(nums)):
            #Compare
            if nums[val] != val: #If our current number isnt equal to what it is suppose to be
                return val
        #Write a condition when there is no missing number
            else: #If our current iteration is equal to its index
                no_missing_num += 1
         #If there are no missing numbers
        return no_missing_num