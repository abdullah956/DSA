from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result=[1]
        for i in range(1,rowIndex+1) :
            result.append(1)
            for j in range(len(result)-2,0,-1) : #start stop step
                result[j]+=result[j-1]
        return result