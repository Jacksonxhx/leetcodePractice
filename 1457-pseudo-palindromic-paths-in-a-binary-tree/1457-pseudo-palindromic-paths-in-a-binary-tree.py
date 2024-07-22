# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        """
        dfs，到leaf检查at most one digit has odd frequency
        """
        if not root:
            return 0
        
        stack = [(root, {})]
        res = 0
        
        while stack:
            node, path_count = stack.pop()
            
            # 更新当前路径上的节点值频率
            path_count = path_count.copy()  # 复制当前路径上的频率字典
            path_count[node.val] = path_count.get(node.val, 0) + 1
            
            # leaf
            if not node.left and not node.right:
                # 统计所有frequency是奇数的和
                odd_count = sum(1 for count in path_count.values() if count % 2 == 1)
                if odd_count <= 1:
                    res += 1
                
            if node.left:
                stack.append((node.left, path_count))
            if node.right:
                stack.append((node.right, path_count))
            
        return res
                    