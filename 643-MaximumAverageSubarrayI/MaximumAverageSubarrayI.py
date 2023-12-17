from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        for i in range(k):
            print("index",i)
            print("first k :",nums[i])
            curr+=nums[i]
            print("first k sum :",curr)
        maxx = curr
        print("first k max :",maxx)
        print()
        for i in range(k,len(nums)):
            print("index i :",i)
            print("last k :",nums[i])
            print("current : ",curr)
            print("k-i : ",nums[i-k])
            curr += nums[i] - nums[i-k]
            print("current : ",curr)
            print("maxx :",maxx)
            if curr>maxx:
                maxx = curr
                print("maxx after swap :",maxx)
        return maxx/k        
nums = [1,12,-5,-6,50,3]
k = 4
s=Solution()
print(s.findMaxAverage(nums,2))