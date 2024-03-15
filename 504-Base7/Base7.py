class Solution :
    def convertToBase7(self,num :int)->str :
        result = ""
        n=num
        print(n)
        num=abs(num)
        print(num)
        if num==0 :
            return "0"
        while num > 0 :
            remaind = num % 7
            print("remainder",remaind)
            result += str(remaind)
            print("result",result)
            num //= 7
            print("num after dividing to 7 :",num)
        if n<0 :
            print("-"+result[::-1])
            return "-"+result[::-1]
        else :
            print(result[::-1])
            return result[::-1]

s = Solution()
print(s.convertToBase7(202))