# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        self.prefix(root, res)
        
        tmp = root
        for i in range(1, len(res)):
            new = TreeNode(res[i])
            tmp.left = None
            tmp.right = new
            tmp = tmp.right
    
    
    def prefix(self, root: Optional[TreeNode], res: list[int]) -> None:
        if root:
            res.append(root.val)
            self.prefix(root.left, res)
            self.prefix(root.right, res)