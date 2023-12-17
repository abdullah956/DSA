from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=[]
        sum = 0
        for val in nums1:
            merged.append(val)
        for val in nums2:
            merged.append(val)
        merged = sorted(merged)
        if (len(merged)%2)==0:
            while len(merged)>2:
                merged.pop(0)
                merged.pop(-1)
        else:
            while len(merged)>1:
                merged.pop(0)
                merged.pop(-1)
        for digit in merged :
            sum += digit
        return (float(sum)/(len(merged)))