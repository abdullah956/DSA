class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1 :
            return n
        previous1,previous2=1,0
        for i in range(2,n+1) :
            output=previous1+previous2
            previous2=previous1
            previous1=output
        return output
    
    def fib (n ) :
        if n==0 or n==1 :
            return n
        prev , prev2 = 1,0
        for i in range(2,n+1) :
            output = prev+prev2
            prev2 == prev
            prev = output
        return output