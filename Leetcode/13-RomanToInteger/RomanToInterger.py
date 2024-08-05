class Solution:
    def romanToInt(self, s: str) -> int:
        Map = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res = 0
        for i in range(len(s)) :
            if i+1 < len(s) and Map[s[i]] < Map[s[i+1]] :
                res -= Map[s[i]]
            else :
                res += Map[s[i]]
        return res  
s = Solution()
romanvalues = input("enter values in roman from (I,V,X,L,C,D,M)\n")
integervalue2 = s.romanToInt(romanvalues)
print("sum : ",integervalue2)
