# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        
        min_depth = float("inf")
        if root.left:
            min_depth = min(l, min_depth)
        if root.right:
            min_depth = min(r, min_depth)

        # 当前节点的最小叶子节点深度
        return min_depth + 1
        