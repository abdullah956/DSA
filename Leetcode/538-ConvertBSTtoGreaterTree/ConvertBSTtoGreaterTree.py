
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        curSum = 0
        def dfs(root:TreeNode) -> int :
            if not root :
                return 0
            nonlocal curSum
            dfs(root.right)
            temp = root.val #saving node value for later
            root.val += curSum #adding cursum to node val
            curSum += temp #cursum will be added by value the node had not by its value now
            dfs(root.left)
        dfs(root)
        return root



