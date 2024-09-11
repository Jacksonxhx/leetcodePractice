# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # 先建哈希表
        hasht = defaultdict(lambda: [None, None])
        
        # 确定所有的根结点
        nodes = dict()  # 保存所有创建的节点
        child_set = set()  # 用于确定根节点
        
        for parent, child, position in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(val=parent)
            if child not in nodes:
                nodes[child] = TreeNode(val=child)
            
            if position == 1:  # position 1 表示左子节点
                nodes[parent].left = nodes[child]
            else:  
                nodes[parent].right = nodes[child]
            
            child_set.add(child)  # 记录所有的子节点
        
        # 寻找根节点，根节点一定不在 child_set 中
        for parent in nodes:
            if parent not in child_set:
                return nodes[parent]
        
        return None
            
            
                