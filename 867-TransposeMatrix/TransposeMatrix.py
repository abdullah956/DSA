from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row , col = len(matrix) , len(matrix[0])
        output = [[0]*row for i in range(col)]
        for r in range(row) :
            for c in range(col) :
                output[c][r] = matrix[r][c]
        return output