class Solution:
    def isPalindrome(self, s: str) -> bool:
        our = ""
        for i in range(len(s)) :
            if s[i].isalnum() :
                our +=s[i]
                
        our = our.lower()
        left,right=0,len(our)-1
        while left <right :
            if our[left] != our[right] :
                return False
            left+=1
            right-=1
        return True