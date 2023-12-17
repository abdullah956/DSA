import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        q = collections.deque()
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                curNode = q.popleft()
                if (curNode.left):
                    q.append(curNode.left)
                if (curNode.right):
                    q.append(curNode.right)
                level.append(curNode.val)
            ans.append(sum(level)/len(level))
        return ans