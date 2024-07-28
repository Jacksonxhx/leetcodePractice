# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode()
        walk = dummy
        
        def inorder(node):
            nonlocal walk
            if node:
                inorder(node.left)
                node.left = None
                walk.right = node
                walk = walk.right
                inorder(node.right)
        
        inorder(root)
        return dummy.right