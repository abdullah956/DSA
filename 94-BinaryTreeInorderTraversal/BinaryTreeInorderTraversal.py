# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
class Solution:
    def inorderTraversal(self, root) -> List[int]:
        result = []
        stack = [] 
        current_node = root 
        while current_node or stack :
            while current_node :
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            result.append(current_node.val)
            current_node = current_node.right
        return result