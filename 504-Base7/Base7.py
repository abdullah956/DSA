class Solution :
    def convertToBase7(self,num :int)->str :
        result = ""
        n=num
        num=abs(num)
        if num==0 :
            return "0"
        while num > 0 :
            remaind = num % 7
            result += str(remaind)
            num //= 7
        if n<0 :
            return "-"+result[::-1]
        else :
            return result[::-1]