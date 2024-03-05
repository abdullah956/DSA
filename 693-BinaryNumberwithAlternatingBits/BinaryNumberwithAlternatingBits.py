class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if not n :
            return True
        number = n^(n>>1)
        # 101 right shift 010
        # 101^010 will always give us 111
        # print(101^10)
        # 111 is 7 1000 is 8
        # so if we and them we will get 0
        # not 0 will be 1 and just return it 
        return not number&(number+1)


s=Solution()
print(s.hasAlternatingBits(5))