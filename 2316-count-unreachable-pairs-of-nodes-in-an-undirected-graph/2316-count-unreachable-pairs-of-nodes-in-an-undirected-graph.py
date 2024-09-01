from collections import deque, defaultdict

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # 先找scc，记录每个连通分量的大小
        component_sizes = []
        visited = set()
        
        # 建图
        graph = defaultdict(list)
        for edge in edges:
            v, u = edge[0], edge[1]
            graph[v].append(u)
            graph[u].append(v)
        
        def bfs(start):
            queue = deque([start])
            visited.add(start)
            size = 0
            
            while queue:
                node = queue.popleft()
                size += 1
                
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            return size
        
        # 遍历所有节点，找到连通分量
        for i in range(n):
            if i not in visited:
                component_size = bfs(i)
                component_sizes.append(component_size)
        
        # 计算配对数
        total_pairs = 0
        total_nodes = sum(component_sizes)
        
        for size in component_sizes:
            total_nodes -= size
            total_pairs += size * total_nodes
        
        return total_pairs
            
            