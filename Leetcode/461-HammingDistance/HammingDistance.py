class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor  = x^y
        s = bin(xor)
        s = s.replace("0b"," ")
        count=0
        for i in s :
            if i=="1" :
                count+=1
        return count