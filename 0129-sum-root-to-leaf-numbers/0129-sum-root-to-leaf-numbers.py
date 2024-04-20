# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        DFS遍历 + 记录每个digit
        每次遍历完记录一个res数组
        通过res数组长度和digits决定每次的数是几
        """
        return self.dfs(root, 0)
        
        
    def dfs(self, root, pre_total):
            if not root:
                return 0
            
            total = pre_total * 10 + root.val
            
            if root.left is None and root.right is None:
                return total
            
            return self.dfs(root.left, total) + self.dfs(root.right, total)