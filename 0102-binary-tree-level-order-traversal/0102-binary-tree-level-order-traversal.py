# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        bfs，每次记录整层的值
        """
        if not root:
            return []
        
        queue = [root]
        res = []
        hh, tt = 0, 1
            
        while hh < tt:
            tmp = []
            size = tt - hh
            
            # 遍历这一层的所有节点
            for _ in range(size):
                # append这一层的所有值
                tmp.append(queue[hh].val)
                
                # 在queue中加入下一层的节点
                if queue[hh].left:
                    queue.append(queue[hh].left)
                    tt += 1
                if queue[hh].right:
                    queue.append(queue[hh].right)
                    tt += 1
                
                # 弹出队头
                hh += 1
                
            res.append(tmp)
        
        return res