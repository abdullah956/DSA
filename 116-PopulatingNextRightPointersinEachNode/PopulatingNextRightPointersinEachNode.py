
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        current , Next = root , root.left if root else None
        while current and Next :
            current.left.next = current.right #children connection
            if current.next : #if there is a next
                current.right.next = current.next.left #making connection of next children 
            current = current.next # do this til current comes null
            if not current : #only when we are going to be at the end current is going to be null
                current = Next #moving current to next
                Next = current.left #next moved to nextleftchild
                 
        return root