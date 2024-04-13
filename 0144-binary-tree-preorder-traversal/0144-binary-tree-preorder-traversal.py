# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        path= []
        def traverse(root):
            path.append(root.val)
            if root.left:
                traverse(root.left)
            
            if root.right:
                traverse(root.right)
        
        if root:
            traverse(root)
        return path