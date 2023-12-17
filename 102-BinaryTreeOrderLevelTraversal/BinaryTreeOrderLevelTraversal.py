import collections
from typing import List
class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        if not root :
            return []
        result = []
        Q = collections.deque()
        Q.append(root)
        while Q :
            Q_length = len(Q)
            level = []
            for i in range(Q_length) :
                node = Q.popleft()
                if node :
                    level.append(node.val)
                    Q.append(node.left)
                    Q.append(node.right)
            if level :
                result.append(level)
        return result
                