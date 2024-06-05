# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        DFS搜索，track current path max
        把每条路的max加入一个set，然后统计set的数量
        '''
        # recursion做dfs
        def dfs(node, max_val):
            if not node:
                return 0
            
            # 当前节点是否为max
            is_good = 1 if node.val >= max_val else 0
            
            # 更新节点最大值
            new_max_val = max(max_val, node.val)
            
            left_good = dfs(node.left, new_max_val)
            right_good = dfs(node.right, new_max_val)
            
            return is_good + left_good + right_good
        
        return dfs(root, root.val)
        