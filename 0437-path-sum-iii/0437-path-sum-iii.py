# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        '''
        dfs, 记录每个node能找到targetsum的数量
        对所有的node进行一次dfs查找
        '''
        res = self.inorder(root, targetSum)
            
        return res
    
    def dfs(self, root, cur_sum, targetSum) -> int:
            if not root:
                return 0
            
            cur_sum = cur_sum + root.val
            left, res, right = 0, 0, 0
            
            left = self.dfs(root.left, cur_sum, targetSum)
            right = self.dfs(root.right, cur_sum, targetSum)
            if cur_sum == targetSum:
                res = 1
            
            return left + res + right
    
    def inorder(self, root, targetSum):
        left, res, right = 0, 0, 0
        if root:
            left = self.inorder(root.left, targetSum)
            res = self.dfs(root, 0, targetSum)
            right = self.inorder(root.right, targetSum)
        
        return left + res + right
        