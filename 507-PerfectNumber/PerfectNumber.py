import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        res = 0
        high = int(math.sqrt(num))+1
        for i in range(1,high):
            if num % i == 0:
                res += i
                if i * i != num:
                    res += num//i
        return res-num == num