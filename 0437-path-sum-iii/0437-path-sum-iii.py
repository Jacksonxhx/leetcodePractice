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
        用前缀和做
        '''
        prefix_sum_count = {0: 1}
        
        def dfs(node, current_sum):
            # 初始前缀和为0，出现1次
            if not node:
                return 0
            
            current_sum += node.val
            # 查找前缀和字典中是否有current_sum - targetSum
            paths = prefix_sum_count.get(current_sum - targetSum, 0)
            
            # 更新当前路径和在前缀和字典中的计数
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1
            paths += dfs(node.left, current_sum)
            paths += dfs(node.right, current_sum)
            
            # 回溯，减少当前路径和在前缀和字典中的计数
            prefix_sum_count[current_sum] -= 1
            
            return paths
        
        return dfs(root, 0)
        