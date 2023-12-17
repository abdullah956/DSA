class Solution:
    def isPalindrome (self , x):
        if x == 0 :
            return True
        if x < 0 or x%10==0 : 
            return False
        reversedx = 0
        while(x >= reversedx):
            pop = x % 10
            x = x // 10 # ground division //
            reversedx = (reversedx*10) + pop
        if x == reversedx or x==reversedx//10 :
            return True
        else : 
            return False

s = Solution()
print(s.isPalindrome(125939521))

