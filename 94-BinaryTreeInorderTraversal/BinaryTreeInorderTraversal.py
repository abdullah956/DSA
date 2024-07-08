from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root) -> List[int]:
        result = []  # This will store the values of nodes in inorder sequence
        stack = []  # Stack to keep track of nodes
        current_node = root  # Start with the root node
        
        # Iterate while there are nodes to be processed
        while current_node or stack:
            # Reach the leftmost node of the current_node
            while current_node:
                stack.append(current_node)  # Push the current node to the stack
                current_node = current_node.left  # Move to the left child
            
            # current_node is now None, process the node on top of the stack
            current_node = stack.pop()  # Pop the top node from the stack
            result.append(current_node.val)  # Append the node's value to the result
            
            # We have visited the node and its left subtree, now it's right subtree's turn
            current_node = current_node.right
        
        return result  # Return the final inorder traversal result