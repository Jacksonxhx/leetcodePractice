from typing import List, Set, Dict
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        '''
        当无向图建图，对于root做dfs，如果遇到[0,n]的情况，就cnt ++
        '''
        # 建无向图，同时表示方向
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, True))  # u -> v，True 表示原始方向
            graph[v].append((u, False))  # v -> u，False 表示逆向
            
        visited = set()
        cnt = 0
        
        def dfs(node):
            visited.add(node)
            neighbors = graph[node]
            
            for neighbor, direction in neighbors:
                if neighbor not in visited:
                    # 如果是原始方向，需要改变
                    if direction:
                        nonlocal cnt
                        cnt += 1
                        # 继续搜
                    dfs(neighbor)
            
        dfs(0)
        
        return cnt
        
        
        