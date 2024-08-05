from typing import List
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        res=[]
        numlines=1
        width=0
        for c in s :
            cwidth = widths[ord(c)-ord('a')]
            if cwidth+width>100 :
                numlines+=1
                width=0
            width+=cwidth
        res.append(numlines)
        res.append(width)
        return res