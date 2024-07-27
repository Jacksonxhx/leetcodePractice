# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """
        dfs到leaf记录
        """
        def dfs(node, path):
            if not node:
                return 0
            # 加入path
            path = (path << 1) | node.val
            # leaf
            if not node.left and not node.right:
                return path
            
            # 递归dfs
            return dfs(node.left, path) + dfs(node.right, path)
        
        return dfs(root, 0)
            
            
            