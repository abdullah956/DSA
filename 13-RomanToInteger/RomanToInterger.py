class Solution:
    def romanToInt(self, s: str) -> int:
        Map ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        integervalue=0
        list =[]
        for i in s:
            list.append(i)
        i=0
        while i<len(list):
            if i<len(list)-1 and Map[list[i]]<Map[list[i+1]]:
                integervalue = integervalue + (Map[list[i+1]] - Map[list[i]])
                i += 2
            else:
                integervalue = integervalue + Map[list[i]]
                i += 1
        return integervalue
s = Solution()
romanvalues = input("enter values in roman from (I,V,X,L,C,D,M)\n")
integervalue2 = s.romanToInt(romanvalues)
print("sum : ",integervalue2)
