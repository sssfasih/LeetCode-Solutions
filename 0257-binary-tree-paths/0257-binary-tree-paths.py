# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
            def f( n, path):
                if not n.left and not n.right:
                    path.append(str(n.val))
                    output.append('->'.join(path))
                    path.pop()
                    return
                path.append(str(n.val))
                if n.left:
                    f(n.left,path)
                if n.right:
                    f(n.right,path)
                path.pop()
                return output
        
            output = []
            f(root,[])
            return output