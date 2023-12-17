class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0 :
            return 0
        elif num % 9 == 0 :
            return 9
        else :
            return num % 9

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9 :
            temp =0
            while num :
                temp += num%10
                num //=10
            num = temp
        return num