class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root.left:
                a = dfs(root.left)
            if root.right:
                b= dfs(root.right)     
            if root.val == 2:
                return a or b
            if root.val == 3:
                return a and b
            
            return root.val
        
        return dfs(root)
                