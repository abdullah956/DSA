from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]):
        def createTreeNode(left,right) :
            if left>right :
                return None
            mid = (left+right)//2
            root  = TreeNode(nums[mid])
            root.left = createTreeNode(left,mid-1)
            root.right = createTreeNode(mid+1,right)
            return root
        return createTreeNode(0,len(nums)-1)
    """
    [1,2,3,4,5,6]
    3
    """