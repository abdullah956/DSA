class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ro = len(grid)
        co = len(grid[0])
        res = [[10**9] * (co + 1) for r in range(ro + 1)]
        res[ro - 1][co] = 0
        for r in range(ro - 1, -1, -1):
            for c in range(co - 1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])
        return res[0][0]