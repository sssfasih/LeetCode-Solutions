# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def traverse(root):
            if root.left:
                if not root.left.left and not root.left.right:
                    self.ans+= root.left.val
                else:
                    traverse(root.left)
                
            if root.right:
                traverse(root.right)
         
        traverse(root)
        return self.ans