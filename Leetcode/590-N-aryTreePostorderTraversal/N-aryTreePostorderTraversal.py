"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from typing import List


class Solution:
    def postorder(self, root) -> List[int]:
        s = []
        li=[]
        s.append(root)
        if not root:
            return
        while(s):
            temp = s.pop()
            li.append(temp.val)
            for i in temp.children:
                s.append(i)
        return li[::-1]
class Solution:
    def postorder(self, root) -> List[int]:
        def rec(root):
            if root:
                for c in root.children:
                    rec(c)
                out.append(root.val)
    
        out = []
        rec(root)
        return out