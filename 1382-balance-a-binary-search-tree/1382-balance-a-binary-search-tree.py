# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        先把树按照顺序存到array里
        然后排序后重建二叉平衡树
        """
        # 通过inorder遍历获得排好序的node
        nodes = []
        def inorder(node):
            if node:
                inorder(node.left)
                nodes.append(node)
                inorder(node.right)
        
        inorder(root)
        
        # 用有序数组构建平衡二叉搜索树
        def build_balanced_bst(nodes) -> TreeNode:
            # base case
            if not nodes:
                return None
            # 找到中间的node，也就是应该作为root的
            mid = len(nodes) // 2
            root = nodes[mid]
            # recursion
            root.left = build_balanced_bst(nodes[:mid])
            root.right = build_balanced_bst(nodes[mid+1:])
            return root
        
        return build_balanced_bst(nodes)
        