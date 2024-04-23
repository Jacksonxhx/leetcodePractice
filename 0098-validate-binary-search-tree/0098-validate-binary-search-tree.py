# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def prefix(root, min_v, max_v):
            # Base case
            if root == None:
                return True
            
            # 列出所有错的情况
            if root.val >= max_v or root.val <= min_v:
                return False
            
            # 判断
            return prefix(root.left, min_v, root.val) and prefix(root.right, root.val, max_v)
        
        # min是无限小，max是无限大
        return prefix(root, float('-inf'), float('inf'))
            