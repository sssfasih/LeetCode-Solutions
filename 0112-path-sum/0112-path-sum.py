# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(root,summ):
            summ += root.val
            if root.left:
                if dfs(root.left,summ) == True:
                    return True
                
            if root.right:
                if dfs(root.right,summ) == True:
                    return True
            
            if not root.left and not root.right:
                if summ == targetSum:
                    return True
        
        return dfs(root,0)
        