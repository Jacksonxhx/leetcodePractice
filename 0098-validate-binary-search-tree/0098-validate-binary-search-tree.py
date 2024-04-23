# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def prefix(root, min_v, max_v):
            if root == None:
                return True
            
            if root.val >= max_v or root.val <= min_v:
                return False
            
            return prefix(root.left, min_v, root.val) and prefix(root.right, root.val, max_v)
        
        return prefix(root, float('-inf'), float('inf'))
            