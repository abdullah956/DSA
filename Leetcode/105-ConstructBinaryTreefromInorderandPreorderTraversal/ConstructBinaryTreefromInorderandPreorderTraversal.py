# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        # Step 1: Create the root node from the first element of preorder
        root = TreeNode(preorder[0])
        print(f"Creating root node with value: {root.val}")

        # Step 2: Find the index of the root in the inorder list
        mid = inorder.index(preorder[0])
        print(f"Root value {root.val} found at index {mid} in inorder list")

        # Step 3: Build the left subtree
        left_preorder = preorder[1 : mid + 1]
        left_inorder = inorder[:mid]
        print(f"Left subtree: preorder {left_preorder}, inorder {left_inorder}")
        root.left = self.buildTree(left_preorder, left_inorder)

        # Step 4: Build the right subtree
        right_preorder = preorder[mid + 1 :]
        right_inorder = inorder[mid + 1 :]
        print(f"Right subtree: preorder {right_preorder}, inorder {right_inorder}")
        root.right = self.buildTree(right_preorder, right_inorder)

        return root

# Example usage:
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
solution = Solution()
root = solution.buildTree(preorder, inorder)
