# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        总共三种情况：
        1. p，q在lca的左右两边
        2. p == lca，q在lca的左边或者右边
        3. q == lca，p在lca的左边或者右边
        
        思路：
        根据上面的三种情况进行recursion的分类
        首先base case设计：找到p或者q时返回当前node
        分为当前node为none：直接返回None，意思是p q不在这个子树下
        和不为none：继续左右recursion，然后找对应的case判断
        '''
        # base case, 当找到p或者q时
        if root == p or root == q:
            return root
        
        # 当存在这个lca时
        if root:
            node_left = self.lowestCommonAncestor(root.left, p, q)
            node_right = self.lowestCommonAncestor(root.right, p, q)
            
            # 当p和q在左右两边的时候，返回中间的root as lca，情况1
            if node_left and node_right:
                return root
            # 情况2，3
            # 当左边是空时，返回右子树
            elif not node_left:
                return node_right
            # 当右边是空时，返回左子树
            else:
                return node_left
            
        return None
        
        
        