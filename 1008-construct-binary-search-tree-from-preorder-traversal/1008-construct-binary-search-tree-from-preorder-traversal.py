# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        """
        recursion: 因为preorder比第一个小的都在左，剩下的都在右
        """
        if not preorder:
            return None
        
        def helper(lower, upper):
            nonlocal idx
            
            # 找干净了
            if idx == len(preorder):
                return None
            
            val = preorder[idx]
            # 不属于这个区域的
            if val < lower or val > upper:
                return 
            
            idx += 1
            root = TreeNode(val)
            # left: lower ~ val之间
            root.left = helper(lower, val)
            # right: val ~ upper之间
            root.right = helper(val, upper)
            return root
        
        idx = 0
        return helper(float("-inf"), float("inf"))
        