from typing import List, Set, Dict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        '''
        对于root做dfs，如果遇到[0,n]的情况，就cnt ++
        '''
        # 用邻接表存图
        graph: Dict[int, List[int]] = {i: [] for i in range(n)}
        # 存边
        edges: Set[Tuple[int, int]] = set()
        
        # 假设是一个无向图，append从a到b，从b到a，构建边
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            edges.add((a, b))
        
        self.cnt = 0
        
        def dfs(u: int, parent: int):
            # 遍历所有到u的v
            for v in graph[u]:
                # 如果v是parent，证明是从v到u，所以continue
                if v == parent:
                    continue
                # 如果(u, v)原本就在，意味着从u到v，则需要inverse
                if (u, v) in edges:
                    self.cnt += 1
                # 遍历所有的v，然后把v作为当前node，u作为parent
                dfs(v, u)
        
        dfs(0, -1)
        return self.cnt