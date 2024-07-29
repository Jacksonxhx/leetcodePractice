# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        DFS搜索一样的话可以
        """
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            # 两个值不一样
            if node1.val != node2.val:
                return False
            
            # 检查两种情况：不翻转和翻转
            no_flip = dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
            flip = dfs(node1.right, node2.left) and dfs(node1.left, node2.right)
            
            return no_flip or flip
        
        return dfs(root1, root2)