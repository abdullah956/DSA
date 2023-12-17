class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = 0
        for cs in s: c ^= ord(cs) #ord is ASCII value
        for ct in t: c ^= ord(ct)
        return chr(c) #chr = convert ASCII into character


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict = {}
        for i in s:
            if(i in dict):
                dict[i] += 1
            else:
                dict[i] = 1
        for i in t:
            if(i not in dict or dict[i] == 0):
                return i
            if(i in dict):
                dict[i] -= 1
        return None