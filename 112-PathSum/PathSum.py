class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        def dfs(node , currentsum) :
            if not node :
                return False 
            currentsum = currentsum + node.val
            if not node.left and not node.right :
                return currentsum == targetSum
            return (dfs(node.left,currentsum) or dfs(node.right,currentsum))
        return dfs(root,0)
