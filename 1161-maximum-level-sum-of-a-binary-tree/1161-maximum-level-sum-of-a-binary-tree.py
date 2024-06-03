# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        '''
        BFS然后统计每层的，求max
        '''
        if not root:
            return []

        queue = [root]
        levels = []
        
        while queue:
            level = 0
            size = len(queue)
            for _ in range(size):
                cur = queue.pop(0)
                level += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                    
            levels.append(level)
        
        res, index = float("-inf"), 0
        for i in range(len(levels)):
            if levels[i] > res:
                res, index = levels[i], i
        
        return index + 1
        