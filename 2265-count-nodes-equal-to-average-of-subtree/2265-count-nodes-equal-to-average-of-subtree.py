# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        
        def dfs(node):
            # 可以修改res
            nonlocal res
            
            if not node:
                return [0, 0]
            
            l_res = dfs(node.left)
            r_res = dfs(node.right)
            
            cur_sum, cnt = node.val + l_res[0] + r_res[0], 1 + l_res[1] + r_res[1]
            
            if cur_sum // cnt == node.val:
                res += 1
            
            return cur_sum, cnt
        
        dfs(root)
        
        return res
