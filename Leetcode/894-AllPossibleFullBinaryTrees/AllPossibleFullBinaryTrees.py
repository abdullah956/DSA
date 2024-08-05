from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        Map = {0: [], 1: [TreeNode()]}

        def dfs(n: int) -> List[TreeNode]:
            if n in Map:
                return Map[n]
            res = []
            for l in range(n):
                r = n - 1 - l
                lt, rt = dfs(l), dfs(r)
                for t1 in lt:
                    for t2 in rt:
                        res.append(TreeNode(0, t1, t2))
            Map[n] = res
            return res

        return dfs(n)


s = Solution()
print(s.allPossibleFBT(3))
