from typing import List
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat_list = []
        matrix = []
        print(nums)
        for sublist in nums:
            for item in sublist:
                flat_list.append(item)

        if len(flat_list) != r * c:
            return nums
        else:
            for i in range(0,len(flat_list),c):
                matrix.append(flat_list[i:i+c])
        return matrix
