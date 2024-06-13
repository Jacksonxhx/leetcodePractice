# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def checkBalance(node):
            if not node:
                return 0
            
            l = checkBalance(node.left)
            if l == -1:
                return -1
            
            r = checkBalance(node.right)
            if r == -1:
                return -1
            
            if abs(l - r) > 1:
                return -1
            
            return max(l, r) + 1
        
        return checkBalance(root) != -1