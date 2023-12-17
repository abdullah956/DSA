
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head :
            return None
        if not head.next :
            return TreeNode(head.val)
        prev , slow , fast = None , head , head
        while fast and fast.next :
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        root = TreeNode(slow.val)
        root.right = self.sortedListToBST(slow.next)
        root.left = self.sortedListToBST(head)
        return root