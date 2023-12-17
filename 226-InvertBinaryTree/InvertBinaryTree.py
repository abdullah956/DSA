# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        if not root :
            return None
        stack = [root]
        while len(stack) > 0 :
            node = stack.pop()
            if node :
                temp = node.left
                node.left = node.right
                node.right = temp
                stack.append(node.left)
                stack.append(node.right)
        return root

class Solution:
    def invertTree(self, root):
        if not root :
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root