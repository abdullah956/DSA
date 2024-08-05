class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Initialize the result with the smallest possible value
        res = [root.val]

        # Define the depth-first search function
        def dfs(node):
            if not node:
                return 0

            # Recursively find the maximum path sum for left and right children
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            
            # Only include positive contributions to the path sum
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Update the result with the maximum path sum including the current node
            res[0] = max(res[0], node.val + leftMax + rightMax)

            # Return the maximum path sum without splitting
            return node.val + max(leftMax, rightMax)

        # Call the dfs function starting from the root
        dfs(root)
        return res[0]

# Example usage:
# Constructing the binary tree [1,2,3]
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

# Constructing the binary tree [-10,9,20,null,null,15,7]
root2 = TreeNode(-10)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)

sol = Solution()
print(sol.maxPathSum(root1))  # Output: 6
print(sol.maxPathSum(root2))  # Output: 42
