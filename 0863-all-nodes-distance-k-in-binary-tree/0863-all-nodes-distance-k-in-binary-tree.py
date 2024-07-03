# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


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
        
        # value + level
        queue = deque([(target.val, 0)])
        visited = set()
        visited.add(target.val)
        res = []
        
        while queue:
            current, distance = queue.popleft()
            
            if distance == k:
                res.append(current)
            elif distance < k:
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, distance + 1))
        
        return res