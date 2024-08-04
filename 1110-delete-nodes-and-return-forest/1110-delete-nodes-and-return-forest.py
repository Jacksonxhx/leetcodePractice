# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        """
        用hash建图
        """
        ans = []
        # O1查找
        s = set(to_delete)
        
        # 写一个dfs，后续遍历
        # 时候后续遍历是确保在处理当前节点之前，其所有子节点已经被处理过
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node: return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            # 如果不需要删除，正常返回
            if node.val not in s: return node
            # 处理需要删除的node
            if node.left: ans.append(node.left)
            if node.right: ans.append(node.right)
            return None
        
        # 处理跟节点
        if dfs(root): ans.append(root)
            
        return ans