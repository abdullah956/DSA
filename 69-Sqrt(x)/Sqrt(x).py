class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==0 or x==1 :
            return x
        start = 1
        end = x
        while start <= end :
            mid = (start+end)//2
            mid_sqrt  = mid*mid
            if mid_sqrt==x :
                return mid
            if mid_sqrt < x :
                start  = mid +1 
                #storing answer by mid because the loop will be exited in next iteration
                answer = mid
            else :
                end = mid -1
        return answer
s = Solution()
print(s.mySqrt(8))