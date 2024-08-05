# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
class Solution:
    def postorderTraversal(self, root) -> List[int]:
        if not root :
            return []
        stack = [root]
        result  = []
        while stack :
            temp = stack.pop()
            result.insert(0,temp.val)
            if temp.left :
                stack.append(temp.left)
            if temp.right :
                stack.append(temp.right)
        return result