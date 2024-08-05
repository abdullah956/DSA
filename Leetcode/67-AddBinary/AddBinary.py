class Solution :
    def addBinary(self, a:str, b:str)-> str:
        res = ""
        carry = 0
        a,b=a[::-1],b[::-1]
        for i in range(max(len(a),len(b))) :
            if i < len(a) :
                digitA = ord(a[i])-ord("0")
            else :
                digitA = 0
            if i < len(b) :
                digitB = ord(b[i])-ord("0")
            else :
                digitB = 0
            total = digitA+digitB+carry
            char = str(total%2)
            res = char + res
            carry = total // 2
        if carry :
            res = "1"+res
        return res
s = Solution()
print(s.addBinary('a','koo'))
