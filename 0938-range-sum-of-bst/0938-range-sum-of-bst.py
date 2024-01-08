# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        summ = 0
        
        def traverse(root,summ):
            if root.val >= low and root.val <= high:
                summ += root.val
            if root.left:
                summ = traverse(root.left,summ)
            if root.right:
                summ = traverse(root.right,summ)
            return summ   
                
        return traverse(root,summ)
        
                
        