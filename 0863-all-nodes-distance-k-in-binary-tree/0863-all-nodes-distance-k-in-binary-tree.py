# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        先建图，用bfs
        """
        def build_graph(node, parent):
            if node:
                # 无向图
                if parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)
                build_graph(node.left, node)
                build_graph(node.right, node)
        
        graph = defaultdict(list)
        build_graph(root, None)
        
        queue = [(target.val, 0)]
        visited = set()
        visited.add(target.val)
        res = []
        
        while queue:
            cur, dist = queue.pop(0)
            
            if dist == k:
                res.append(cur)
            
            for neighbor in graph[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        
        return res