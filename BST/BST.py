from typing import List
class TreeNode :
    val = 0
    left = None
    right = None
    def __init__(self,val:int)->None:
        self.val = val
        self.left = None
        self.right = None
    root = None
    def takeRoot(self):
        return self.root
    def returnRoot(self,root):
        self.root = root
    def insert(self, root, val):
        if not root : 
            self.returnRoot(TreeNode(val))
            return
            #return self.returnRoot(TreeNode(val))
        def insertintoBST(node,val) :
            if val > node.val :
                if not node.right :
                    node.right = TreeNode(val)
                else :
                    insertintoBST(node.right,val)
            else :
                if not node.left :
                    node.left = TreeNode(val)
                else :
                    insertintoBST(node.left,val)
        insertintoBST(root,val)
        #return root#self.returnRoot(root)
    
    def searchBST(self, root, val: int):
        if not root : 
            return None
        if root.val==val :
            return root
        if val < root.val :
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)
    
    def getMin(self,root) :
        current = root
        while current.left :
            current = current.left
        return current
    def deleteNode(self, root, key: int):
        if not root :
            return root
        elif key < root.val :
            root.left = self.deleteNode(root.left,key)
        elif key > root.val :
            root.right = self.deleteNode(root.right,key)
        else :
            if not root.left and not root.right :
                root = None
            elif not root.left :
                root = root.right
            elif not root.right :
                root = root.left
            else :
                temp = self.getMin(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right,temp.val)
        return root
    def inorderTraversal(self, root) -> List[int]:
        if not root :
            return []
        stack = []
        result=[]
        while root or stack :
            while root :
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result
    def preorderTraversal(self, root) -> List[int]:
        if not root :
            return []
        stack=[root]
        result=[]
        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.right :
                stack.append(root.right)
            if root.left :
                stack.append(root.left)
        return result
    def postorderTraversal(self, root) -> List[int]:
        if not root :
            return []
        stack = [root]
        result =[]
        while stack :
            root = stack.pop()
            result.insert(0,root.val) 
            if root.left :
                stack.append(root.left)
            if root.right :
                stack.append(root.right)
        return result
    def levelOrder(self, root) -> List[List[int]]:
        if not root :
            return []
        Q,nextQ,level,result = [root],[],[],[]
        while Q :
            for root in Q : 
                level.append(root.val)
                if root.left :
                    nextQ.append(root.left)
                if root.right :
                    nextQ.append(root.right)
            result.append(level)
            level=[]
            Q=nextQ
            nextQ=[]
        return result
tree = TreeNode(None)
tree.insert(tree.takeRoot(),89)
tree.insert(tree.takeRoot(),-89)
tree.insert(tree.takeRoot(),890)
tree.insert(tree.takeRoot(),-90)
tree.insert(tree.takeRoot(),-70)
tree.insert(tree.takeRoot(),895)
tree.insert(tree.takeRoot(),880)
tree.root = tree.deleteNode(tree.root,89)
print("inorder traversal : ",tree.inorderTraversal(tree.takeRoot()))
print("preorder traversal : ",tree.preorderTraversal(tree.takeRoot()))
print("postorder traversal : ",tree.postorderTraversal(tree.takeRoot()))
print("levelorder traversal :",tree.levelOrder(tree.takeRoot()))
print("search : ",(tree.searchBST(tree.takeRoot(),880)).val)