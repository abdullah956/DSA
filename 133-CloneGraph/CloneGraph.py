
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        Map = {}
        def clone(node:Node) -> Node:
            if node in Map :
                return Map[node]
            copy = Node(node.val)
            Map[node] = copy
            for n in node.neighbors :
                copy.neighbors.append(clone(n))
            return copy
        return clone(node) if node else None
