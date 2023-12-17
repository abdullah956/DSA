from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums :
            i = abs(n)-1
            print(i)
            nums[i] = -1*abs(nums[i])
            print(nums[i])
        result  =[]
        for i , n in enumerate(nums) :
            print(i)
            print(n)
            if n>0 :
                result.append(i+1)
        return result
s = Solution()
num = [1,2,3,3]
print(s.findDisappearedNumbers(num))