class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        queue = deque()
        queue.append([root, 0])
        prev, lvl = None, -1
        while queue:
            current, level = queue.popleft()
            if current.left:
                queue.append([current.left, level + 1])
            if current.right:
                queue.append([current.right, level + 1])
            if prev and level == lvl:
                prev.next = current
            prev, lvl = current, level
        return root  
