from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res,count=0,0
        for n in nums:
            if count==0 :
                res=n
            if n==res :
                count+=1
            else :
                count-=1
        return res
"""
[3,2,3]
n 3 
res 3
count 1
n 2 
res 3
count 0
n 3 
res 3 
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Map = dict()
        res,maxcount = 0,0
        for n in nums :
            Map[n] = 1 + Map.get(n,0)
            if Map[n] > maxcount :
                res = n
            maxcount = max(maxcount,Map[n])
        return res