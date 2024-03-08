# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        def traverse(root):
            if not root: return
            if root.left:
                traverse(root.left)
            lst.append(root.val)
            if root.right:
                traverse(root.right)
        traverse(root)
        return lst
        