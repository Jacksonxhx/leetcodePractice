# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_length = 0
        
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        '''
        用dfs做，dp的思想，统计每个node最长的zigzag长度
        '''
        def dfs(node, direction, length):
            if not node:
                return 
            # 更新最长的zigzag
            self.max_length = max(length, self.max_length)
            
            # 如果当前方向是向左，则下一步移动到右子节点（0左1右）
            if direction == 0:  
                # 处理往右和失败的情况
                dfs(node.right, 1, length + 1)  # 改变方向向右
                dfs(node.left, 0, 1)  # 重新开始计算从当前节点向左的路径
            else: 
                # 处理往左和失败的情况
                dfs(node.left, 0, length + 1)  # 改变方向向左
                dfs(node.right, 1, 1)  # 重新开始计算从当前节点向右的路径
            
        # 从根节点开始，初始化方向向左和向右
        dfs(root, 0, 0)  # 从根节点开始，向左的路径
        dfs(root, 1, 0)  # 从根节点开始，向右的路径
        
        return self.max_length