from collections import deque

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # 构建无向图
        graph = {i: [] for i in range(n)}
        
        # 填充图的边
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        restricted_set = set(restricted)
        
        # BFS初始化
        visited = set()
        queue = deque([0])
        visited.add(0)
        res = 0
        
        while queue:
            node = queue.popleft()
            res += 1
            
            for neighbor in graph[node]:
                if neighbor not in restricted_set and neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        
        return res
                