from collections import defaultdict

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # 找到有几个unconnected的computer cluster，找scc数量，return数量就行
        length = len(connections)
        
        # 处理不可能的情况 
        if length + 1 < n:
            return -1
        
        # 建图
        graph = {}
        for i in range(n):
             graph[i] = []
        
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)
        
        clusters = []
        visited = set()
        
        def dfs(i):
            connects = graph[i]
            group = set()
            
            while connects:
                connect = connects.pop()
                
                if connect not in group:
                    connects += graph[connect]
                    group.add(connect)
                    visited.add(connect)
                
            clusters.append(group)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
        
        print(clusters)
        
        return len(clusters) - 1
        