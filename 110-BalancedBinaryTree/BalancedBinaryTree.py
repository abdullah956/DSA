class Solution:
    def isBalanced(self, root) -> bool:
        def dfs(root) :
            if not root :
                return [True,0]
            leftst = dfs(root.left) 
            rightst = dfs(root.right)
            balanced = (leftst[0] and rightst[0] and abs(leftst[1] - rightst[1])<=1)
            return [balanced , 1+max(leftst[1],rightst[1])]
        return dfs(root)[0]