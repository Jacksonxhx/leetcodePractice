# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS回溯
        
        def deep(node):
            if not node:
                return 0, None
            
            # recursion
            l, r = deep(node.left), deep(node.right)
            
            # 如果左边比右边高
            if l[0] > r[0]:
                return l[0] + 1, l[1]
            elif l[0] < r[0]:
                return r[0] + 1, r[1]
            # 如果两边一样高
            else:
                return l[0] + 1, node
        
        return deep(root)[1]