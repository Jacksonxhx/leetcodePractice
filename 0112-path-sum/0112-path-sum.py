# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        dfs，然后记录所有的sum，然后找
        '''
        if root is None:
            return False
        
        res = []
        visited = []
        
        def dfs(node, Sum):
            if node in visited:
                Sum -= node.val
                return
            
            if node is None:
                return
            
            Sum += node.val
            visited.append(node)
            
            if node.left is None and node.right is None:
                res.append(Sum)
                Sum -= node.val
                return
            
            dfs(node.left, Sum)
            dfs(node.right, Sum)
        
        dfs(root, 0)
        print(res)
        
        if targetSum in res:
            return True
        
        return False