from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0  # Variable to keep track of the maximum area
        stack = []  # Stack to store pairs of (index, height)

        # Iterate through each bar in the histogram
        for i, h in enumerate(heights):
            start = i  # Start position for the current bar
            # While stack is not empty and the height of the bar at the top of the stack is greater than the current bar's height
            while stack and stack[-1][1] > h:
                index, height = stack.pop()  # Pop the top of the stack
                # Calculate the area with the popped bar as the smallest height
                maxArea = max(maxArea, height * (i - index))
                # The start position for the current bar becomes the index of the popped bar
                start = index
            # Push the current bar along with the updated start position onto the stack
            stack.append((start, h))

        # After processing all bars, calculate the area for the remaining bars in the stack
        for i, h in stack:
            # The width for these bars extends to the end of the histogram
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea  # Return the maximum area found
