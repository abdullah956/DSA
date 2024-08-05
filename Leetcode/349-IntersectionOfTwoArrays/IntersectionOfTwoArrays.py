from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = set(nums1), set(nums2)
        ans_list = []
        for i in nums1:
            if i in nums2:
                ans_list.append(i)
        return ans_list