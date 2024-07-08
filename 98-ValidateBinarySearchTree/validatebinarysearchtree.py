# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self._isValidBST(root, float('-inf'), float('inf'))
    
    def _isValidBST(self, node: TreeNode, low: float, high: float) -> bool:
        if not node:
            return True
        
        val = node.val
        if val <= low or val >= high:
            return False
        
        if not self._isValidBST(node.right, val, high):
            return False
        if not self._isValidBST(node.left, low, val):
            return False
        
        return True