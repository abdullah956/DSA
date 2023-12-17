class Solution:
    def findComplement(self, num: int) -> int:
        n = bin(num)[2:] #removing frist 2 characters
        s = ''
        for i in n:
            if i == '0':
                s = s + '1'
            else:
                s = s + '0'
        return int(s,2) #type casting to int with base 2
