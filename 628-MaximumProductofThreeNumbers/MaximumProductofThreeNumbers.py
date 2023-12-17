from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        N=len(nums)
        print(N)
        print(nums[N-1])
        print(nums[0])
        print(nums[1])
        p1 = nums[N-1]*nums[0]*nums[1]
        print(p1)
        print(nums[N-1])
        print(nums[N-2])
        print(nums[N-3])
        p2 = nums[N-1]*nums[N-2]*nums[N-3]
        print(p2)
        return max(p1,p2)
s = Solution()
num = [-5,-6,1,2,3,4,5]
print(s.maximumProduct(num))