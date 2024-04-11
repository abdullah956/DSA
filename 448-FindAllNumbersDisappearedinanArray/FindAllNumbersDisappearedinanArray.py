from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums :
            i = abs(n)-1
            print("after -1 ",i)
            nums[i] = -1*abs(nums[i])
            print("value after multipling",nums[i])
        result  =[]
        print(nums)
        for i , n in enumerate(nums) :
            print("index",i)
            print("value at index",n)
            if n>0 :
                result.append(i+1)
        return result
s = Solution()
num = [3,3,2,1]
print(s.findDisappearedNumbers(num))