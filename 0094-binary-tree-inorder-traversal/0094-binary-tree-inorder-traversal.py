# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        lst = []
        def traverse(root):
            if root.left:
                traverse(root.left)
            lst.append(root.val)
            if root.right:
                traverse(root.right)
        traverse(root)
        return lst
        