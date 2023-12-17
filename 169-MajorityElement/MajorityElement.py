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