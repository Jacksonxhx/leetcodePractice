# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        用dfs的方式依次检查每一个node
        '''
        if not root:
            return True
        
        def checkBalance(node) -> int:
            # 到最下一层，直接返回0
            if not node:
                return 0
            
            # 判断左右两个子树是否有node
            l = checkBalance(node.left)
            if l == -1:
                return -1
            
            r = checkBalance(node.right)
            if r == -1:
                return -1
            
            # 证明height not balanced
            if abs(l - r) > 1:
                return -1
            
            return max(l, r) + 1
        
        return checkBalance(root) != -1
            
        
        