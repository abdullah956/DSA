from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.right :
                q.append(node.right)
            if node.left :
                q.append(node.left)
        return node.val
    
"""
                                       1
                                    /    \
                                   2      3
                                  /  \   /  \
                                 4    5 6   7 
"""