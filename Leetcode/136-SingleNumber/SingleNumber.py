from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = dict()
        for num in nums :
            if not num in map :
                map.update({num : 1})
            else:
                map.update({num :map.get(num)+1})
        for num in nums :
            if map.get(num) == 1 :
                return num

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=[]
        for i in nums:
            if i in a:
                a.remove(i)
            else:
                a.append(i)
        return a[0]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result =0 
        for num in nums  :
            result = result ^ num
        return result