# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
class Solution:
    def preorderTraversal(self, root) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

class Solution:
    def preorderTraversal(self, root) -> List[int]:
        if not root :
            return []
        stack=[root]
        result =[]
        while stack :
            root = stack.pop()
            result.append(root.val)
            if root.right :
                stack.append(root.right)
            if root.left :
                stack.append(root.left)
        return result