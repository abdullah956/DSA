class Solution:
    def findTilt(self, root) -> int:
           
        tilt_sum = 0
        
        def helper( node):
            
            if not node:
				# base case: empty node or empty tree
                return 0
            
            else:
                
                left_sum = helper(node.left)
                right_sum = helper(node.right)
                
				# update tilt sum for whloe binary tree
                nonlocal tilt_sum
                tilt_sum += abs(left_sum - right_sum)
				
                return left_sum + node.val + right_sum
        
        # ---------------------------------------------
        
        helper( root )
        return tilt_sum