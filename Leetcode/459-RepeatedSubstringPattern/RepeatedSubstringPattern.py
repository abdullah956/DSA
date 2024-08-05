class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        newstr=s*2
        newstr=newstr[1:-1] # popping first and last
        if s in newstr :
            return True
        else:
            return False