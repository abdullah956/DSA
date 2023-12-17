from typing import List
class Solution :
    def readBinaryWatch(self, turnedOn : int) -> List[str] :
        result = []
        for hours in range (12) :
            for minutes in range (60) :
                if (bin(hours)+bin(minutes)).count("1") == turnedOn :
                    time = '%d:%02d'% (hours, minutes)
                    result.append(time)
        return result