# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = 0
        # 0 不是left， 1 是left
        queue = collections.deque([(root, 0)])
        
        while queue:
            for _ in range(len(queue)):
                node, judge = queue.popleft()
                
                if judge == 1 and not node.left and not node.right:
                    res += node.val
                
                if node.left:
                    queue.append((node.left, 1))
                if node.right:
                    queue.append((node.right, 0))
        
        return res