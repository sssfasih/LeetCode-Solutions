# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def traverse(root,leafs):
            if root:
                if root.left:
                    leafs = traverse(root.left,leafs)
                if root.right:
                    leafs=traverse(root.right,leafs)
                if not root.left and not root.right:
                    leafs.append(root.val)
            return leafs
        
        return traverse(root1,[]) == traverse(root2,[])
                
            
                
                
            
        