# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        """
        DFS从leaf开始回溯
        因为会一直返回deeper的subtree的根节点，所以track最小的
        """
        def deep(root):
            if not root: 
                return 0, None
            # dfs回溯
            l, r = deep(root.left), deep(root.right)
            
            if l[0] > r[0]: 
                return l[0] + 1, l[1]
            # 右高返回右tree height+右边最高的subtree节点
            elif l[0] < r[0]: 
                return r[0] + 1, r[1]
            # 如果一样height，height += 1，返回他们的根节点
            else: 
                return l[0] + 1, root
            
        return deep(root)[1]