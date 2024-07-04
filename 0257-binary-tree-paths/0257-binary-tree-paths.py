# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        DFS
        """
        res = []
        path = []
        
        def dfs(node, path):
            if not node:
                return
            
            path.append(str(node.val))
            
            if not node.left and not node.right:
                res.append("->".join(path))
            else:
                if node.left:
                    dfs(node.left, path)
                if node.right:
                    dfs(node.right, path)
            path.pop()
        
        dfs(root, path)
        
        return res