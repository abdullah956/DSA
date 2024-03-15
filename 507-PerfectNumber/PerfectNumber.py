import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        res = 0
        print("number is : ",num)
        high = int(math.sqrt(num))+1
        print("square root number is : ",high)
        for i in range(1,high):
            print("value of i",i)
            if num % i == 0:
                res += i

                print("result after incrementing i : ",res)
                if i * i != num:
                    print("i * i != num:",i*i)
                    print("res += num//i",res)
                    res += num//i
        print("res",res)
        print("res-num == num",res-num == num)
        return res-num == num
s = Solution()
print(s.checkPerfectNumber(28))