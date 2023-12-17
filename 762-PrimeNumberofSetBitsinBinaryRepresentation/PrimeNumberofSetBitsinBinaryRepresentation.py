class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        countP=0
        for i in range(left,right+1) :
            ans = bin(i).count('1')
            if self.isPrime(ans) :
                countP+=1
        return countP
    def isPrime(self, n : int) -> bool :
        count = 0
        for i in range(1,n+1) :
            if n%i==0 :
                count +=1
        if count ==2:
            return True
        else:
            return False
        