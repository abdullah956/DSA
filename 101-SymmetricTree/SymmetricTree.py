class Solution:
    def isSymmetric(self, root) -> bool:
        if not root  :
            return True
        return  self.mirrorImage(root.left,root.right)
    def mirrorImage(self, leftroot , rightroot) :
        if leftroot and rightroot :
            return leftroot.val == rightroot.val and self.mirrorImage(leftroot.left,rightroot.right) and self.mirrorImage(leftroot.right,rightroot.left)
        return leftroot == rightroot