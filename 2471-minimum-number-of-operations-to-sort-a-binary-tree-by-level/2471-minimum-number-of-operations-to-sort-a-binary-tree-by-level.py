# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        groups = []
        queue = deque([root])
        
        while queue:
            group = []
            
            for i in range(len(queue)):
                node = queue.popleft()
                group.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            groups.append(group)

        def min_swaps_to_sort(arr):
            n = len(arr)
            sorted_arr = sorted(arr)
            # 保存每个值的原始索引
            index_map = {v: i for i, v in enumerate(arr)}
            swaps = 0
            visited = [False] * n
            
            for i in range(n):
                # 如果遇到已经排好的
                if visited[i] or arr[i] == sorted_arr[i]:
                    continue
                
                # 开始计算环的长度
                cycle_size = 0
                x = i
                
                while not visited[x]:
                    visited[x] = True
                    x = index_map[sorted_arr[x]]
                    cycle_size += 1
                
                if cycle_size > 1:
                    swaps += cycle_size - 1
                
            return swaps
                
        res = 0
        # 对每一层的group，计算最少交换次数
        for group in groups:
            res += min_swaps_to_sort(group)
        
        return res