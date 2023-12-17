class Solution:
    def firstUniqChar(self, s: str) -> int:
        dicto={}
        for i in s:
            dicto[i]=1+dicto.get(i,0)
        for i in dicto:
            if dicto[i] == 1:
                return s.index(i)
        return -1