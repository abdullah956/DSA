class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]  # Start with the empty subset

        for num in nums:
            new_subsets = []
            for curr in result:
                new_subsets.append(curr + [num])
            result.extend(new_subsets)

        return result