from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # Find the rightmost element that is smaller than the element to its right
        right_peak = -1
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                right_peak = i
                break

        # If no such element is found, reverse the entire array
        if right_peak == -1:
            nums.reverse()
            return

        # Find the smallest element to the right of right_peak that is greater than nums[right_peak-1]
        index = right_peak
        for i in range(right_peak + 1, n):
            if nums[i] > nums[right_peak - 1] and nums[i] <= nums[index]:
                index = i

        # Swap nums[right_peak-1] and nums[index]
        nums[right_peak - 1], nums[index] = nums[index], nums[right_peak - 1]

        # Reverse the subarray to the right of right_peak-1
        nums[right_peak:] = reversed(nums[right_peak:])


# Example usage:
solution = Solution()

arr = [2, 3, 1, 3, 3]
solution.nextPermutation(arr)
print(arr)  # Output: [2, 3, 3, 1, 3]
