from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)    
        s = n*(n+1)//2   # This code will calculate sum of 1-n numbers. please refer to Arithmetic Progression from Maths
        miss = s - sum(set(nums))  # set(num) will return unique elements from the list and the sum(set(nums)) will calculate the sum of unique elements from the list.
        duplicate = sum(nums) + miss - s # sum(nums) + miss no - sum of 1-n numbers will give us the duplicate
        return [duplicate, miss]