# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(root,level):
            if not root:
                return level
            level += 1
            x,y = 0,0
            if root.left:
                x = traverse(root.left,level)
                
            if root.right:
                y = traverse(root.right,level)
                
            if x > level:
                level = x
            if y > level:
                level = y
            
            return level
        
        
        return traverse(root,0)
        