# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 递归算法，每次交换当前node的左右子node
        
        # Set up base case:
        if root is None:
            return None 
        
        # Swap
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root