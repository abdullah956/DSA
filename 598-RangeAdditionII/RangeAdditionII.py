from typing import List
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row = m
        print("rows",m)
        min_col = n
        print("cloumn",n)
        print("length of ops",len(ops))
        for i in range(len(ops)):
            print("for i =",i)
            print("ops[",i,"][0]","=",ops[i][0])
            min_row=min(min_row, ops[i][0])
            print("minimum rows",min_row)
            print("ops[",i,"][1]","=",ops[i][1])
            min_col=min(min_col, ops[i][1])
            print("minimum columns",min_col)
        print(min_col*min_row)
        return min_row*min_col
s=Solution()
ops = [[2,2],[3,3]]
m=3
n=3
print(s.maxCount(m,n,ops))