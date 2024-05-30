# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum
    
    def dfs(self, node):
        if not node:
            return 0
        
        # Recursively calculate the maximum sum on the left and right subtrees
        left_max = max(self.dfs(node.left), 0)
        right_max = max(self.dfs(node.right), 0)
        
        # Calculate the path sum that includes the current node
        current_sum = node.val + left_max + right_max
        
        # Update the global maximum path sum
        self.max_sum = max(self.max_sum, current_sum)
        
        # Return the maximum path sum where the current node is the endpoint
        return node.val + max(left_max, right_max)