# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Recursive function
        def traverse(node1,node2):
            # if both nodes exists and val equal, proceed
            if node1 and node2 and node1.val == node2.val:
                # we think that left and right are equal
                a,b = True,True
                # if left exists on both sides, traverse it to find equality
                if node1.left and node2.left:
                    a = traverse(node1.left,node2.left)
                # if left exusts on one side only; return False
                elif node1.left or node2.left:
                    return False
                # same conditions as above for right
                if node1.right and node2.right:
                    b= traverse(node1.right,node2.right)
                elif node1.right or node2.right:
                    return False
                # if our initial thinking was wrong, return False
                if a == False or b == False:
                    return False
                # if not returned False till now, return True
                return True    
            else:
                if node1 == node2:
                    return True
                return False
        
        return traverse(p,q)