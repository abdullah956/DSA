class Solution:
    def maxDepth(self, root) -> int:
        stack = [[root,1]]
        result = 0
        while stack :
            node , depth = stack.pop()
            if node :
                result = max(result,depth)
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])
        return result