class Solution:
    def firstUniqChar(self, s: str) -> int:
        Map={}
        for i in s :
            if i in Map :
                Map[i] += 1
            else :
                Map[i] = 1
        for i in Map:

            if Map[i] == 1:
    
                return s.index(i)
        return -1