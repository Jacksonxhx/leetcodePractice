# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        DP的思想，DFS可以做，其实就是求每个root下最大的sum
        每个node的最大和就是由于下面两个最大的和而来的，如果是负数，这个node自身的最大值就是0
        但是如果这个node想要perform左+右，就不能为0，为0只有左右选一遍的时候才可以
        '''
        # 定义全局变量
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum
    
    def dfs(self, node):
        # base case
        if not node:
            return 0
        
        # recursion call，如果小于0则最大是0（不带上这个node）
        left_max = max(self.dfs(node.left), 0)
        right_max = max(self.dfs(node.right), 0)
        
        # 对于当前这个node的最大值
        current_sum = node.val + left_max + right_max
        
        # update global value
        self.max_sum = max(self.max_sum, current_sum)
        
        # 返回当前路线的最大值，因为是path所以不能分叉，只能传一边的
        return node.val + max(left_max, right_max)