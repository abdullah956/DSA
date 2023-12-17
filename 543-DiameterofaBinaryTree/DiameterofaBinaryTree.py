class Solution :
    def diameterOfBinaryTree(self,root)->int :
        result=[0]
        self.diameter(root,result)
        return result[0]
    def diameter(self,root,result) :
        if not root :
            return 0
        left = self.diameter(root.left,result)
        right = self.diameter(root.right,result)
        result[0]= max(result[0],left+right)
        return 1+max(left,right)