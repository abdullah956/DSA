# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
class Solution:
    def binaryTreePaths(self, root) -> List[str]:
        def dfs(root,path):
            if not root.left and not root.right:
                return res.append(path+str(root.val)) 
            if root.left:
                dfs(root.left,path+str(root.val)+"->")
            if root.right:
                dfs(root.right,path+str(root.val)+"->")
        res=[]
        dfs(root,"")
        return res