from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [nums.copy()]
        print("Current nums:", nums)
        for i in range(len(nums)):
            n = nums.pop(0)
            print("Choosing:", n)
            perms = self.permute(nums)
            print("Permutations of remaining nums:", perms)
            for perm in perms:
                perm.append(n)
            print("Appending", n, "to permutations:", perms)
            result.extend(perms)
            nums.append(n)
            print("Result after appending", n, "back to nums:", result)
        return result

# Test
solution = Solution()
nums = [1, 2, 3]
print("All permutations:", solution.permute(nums))
