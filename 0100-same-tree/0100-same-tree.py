# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #定义答案数组用于比较
        valp = []
        valq = []
        
        #用prefix顺序遍历，记录答案到答案数组中
        def prefix(t:TreeNode, val_list: list):
            if t is not None:
                val_list.append(t.val)
                prefix(t.left, val_list)
                prefix(t.right, val_list)
            else:
                val_list.append(None)
        prefix(p, valp)
        prefix(q, valq)
        
        #确保一样，省时间
        if len(valp) != len(valq):
            return False
        #依次比较
        for i in range(len(valp)):
            if valp[i] != valq[i]: 
                return False
        
        return True
                