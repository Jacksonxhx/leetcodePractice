# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        bfs，记录层数，奇数层inverse
        '''
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            tmp = []
            for i in range(level_size):
                node = queue.popleft()
                
                tmp.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            res.append(tmp)
            
        for i in range(len(res)):
            if i % 2 == 1:
                res[i] = res[i][::-1]
            
        return res