from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers)-1
        while a <= b :
            sum = numbers[a] + numbers[b]
            if sum>target :
                b = b - 1
            elif sum<target :
                a = a + 1
            else :
                return [a+1,b+1]
        return [a+1,b+1]

s = Solution()
nums = [ 2,7,11,15 ]
target = 9
nums2 = s.twoSum(nums,target)
print(nums2)
