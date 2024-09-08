from collections import defaultdict

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # 找到有几个unconnected的computer cluster，找scc数量，return数量就行
        
        # 处理不可能的情况 
        if len(connections) < n - 1:
            return -1
        
        # 构建图
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        # 访问过的节点集合
        visited = set()
        
        # 深度优先搜索
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        # 统计有多少个连通分量
        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)
        
        return components - 1
        