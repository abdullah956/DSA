from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals based on the starting time of each interval
        intervals.sort(key=lambda x: x[0])
        
        # Initialize an empty list to store the merged intervals
        merged = []
    
        # Iterate through each interval in the sorted list
        for interval in intervals:
            # If the merged list is empty or the last interval in merged does not overlap with the current interval
            if not merged or merged[-1][1] < interval[0]:
                # Append the current interval to merged as it doesn't overlap with the last interval in merged
                merged.append(interval)
            else:
                # If there is an overlap, merge the current interval with the last interval in merged
                # by updating the end time to the maximum end time between the two intervals
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        # Return the list of merged intervals
        return merged
