class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root : TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # returns tail
        def dfs(root) :
            if not root :
                return None
            leftT = dfs(root.left)
            rightT = dfs(root.right)
            if root.left :
                leftT.right = root.right #attaching left side with right
                root.right = root.left #attaching left with root than
                root.left = None #making left side none
            last = rightT or leftT or root #it is truethat we are going to return the righttail
            return last
        dfs(root)