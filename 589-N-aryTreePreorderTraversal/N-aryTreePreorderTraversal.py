"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from typing import List


class Solution:
    def preorder(self, root) -> List[int]:
        if root is None:
            return []
        stack = [root]
        output = []
        while stack:
            temp = stack.pop()
            output.append(temp.val)
            stack.extend(temp.children[::-1])
        return output
class Solution:
    def preorder(self, root) -> List[int]:
        output =[]
        self.dfs(root, output)
        return output
    def dfs(self, root, output):
        if root is None:
            return
        output.append(root.val)
        for child in root.children:
            self.dfs(child, output)
       