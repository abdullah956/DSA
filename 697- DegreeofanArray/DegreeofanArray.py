from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count={}
        start={}
        end={}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]]=1
                start[nums[i]]=i
                end[nums[i]]=i
            else:
                count[nums[i]]+=1
                end[nums[i]]=i
        res=[]
        maxm=max(list(count.values()))
        for i,j in count.items():
            if j==maxm:
                d=end[i]-start[i]+1
                res.append(d)
        return min(res)