class Solution:
    def rotate(self,nums,k):
        k = k % len(nums)
        self.rev(nums, 0 , len(nums)-1)
        self.rev(nums, 0 , k-1)
        self.rev(nums, k , len(nums)-1)
    def rev(self, nums, start , end):
        while start < end :
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start = start +1
            end = end - 1
s = Solution ()
nums = [1,2,3,4,5,6,7]
k = 3
print(s.rotate(nums,k))
print(nums)

"""
[1,2,3,4,5,6,7]
0-len
[7,6,5,4,3,2,1]
0-k reverse 
[5,6,7,4,3,2,1]
k-len reverse
[5,6,7,1,2,3,4]
"""

