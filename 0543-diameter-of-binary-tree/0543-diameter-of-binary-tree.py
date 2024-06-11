# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        左边的height + 右边的height = diameter
        '''
        self.diameter = 0
        
        def find_height(node):
            # 如果是空返回0
            if not node:
                return 0
            
            # 遍历左右高度
            left_height = find_height(node.left)
            right_height = find_height(node.right)
            
            # 每次更新一轮
            self.diameter = max(self.diameter, left_height + right_height)
            
            return max(left_height, right_height) + 1
        
        find_height(root)
        return self.diameter
            