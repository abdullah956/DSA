from typing import List 
class Solution :
    def findPoisonedDuration(self, timeSeries:List[int], duration:int)->int :
        if  not timeSeries :
            return 0
        total_duration = 0
        for i in range(len(timeSeries)-1):
            poisoned = min (duration , timeSeries[i+1]-timeSeries[i])
            total_duration += poisoned
        total_duration += duration
        return total_duration