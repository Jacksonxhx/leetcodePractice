# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        self.infix(root, inorder)
        print(inorder)
        
        return inorder[k - 1]
    
    def infix(self, root: Optional[TreeNode], inorder: list[int]) -> None:
        if root:
            self.infix(root.left, inorder)
            inorder.append(root.val)
            self.infix(root.right, inorder)