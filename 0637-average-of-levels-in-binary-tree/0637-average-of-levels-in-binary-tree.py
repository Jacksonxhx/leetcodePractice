# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # BFS
        queue = []
        res = []
        queue.append(root)
        
        # BFS 模版
        while queue:
            qlen = len(queue)
            tmp = 0
            
            # 每一层的循环
            for i in range(qlen):
                # 取出队头
                node = queue.pop(0)
                
                # 记录这一层的所有值
                tmp += node.val
                
                # 每次都把下一层的所有node加入queue中
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # append每一层的avg
            res.append(tmp/qlen)
                
        return res