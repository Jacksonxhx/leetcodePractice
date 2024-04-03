# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        按照BFS算法便利，把每一层的最后一个node加入res
        """
        # 对于root = []情况做判断
        if not root:
            return []
        
        # initialize a queue
        queue = [root]
        res = []
        
        # BFS
        while queue:
            # 取出这一层有几个node，用来判断最后一个node的index是几
            size = len(queue)
            # 每层添加下一层的node
            for i in range(size):
                # 得到当前node
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            # 当找到每一层最右边的值之后，append到res中
            if i == size - 1:
                res.append(cur.val)
        
        return res
        