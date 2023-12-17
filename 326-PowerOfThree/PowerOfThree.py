class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0 :
            return False
        x = 1
        i = 1
        
        while x <= n :
            if x==n :
                return True
            x=3**i
            i+=1
        return False
    #return n>0 and (3**19)%n==0