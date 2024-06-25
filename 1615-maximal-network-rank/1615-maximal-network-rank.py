class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        """
        找最大的的入度pair
        找到之后判断是否相连，如果相链 max--
        
        用邻接矩阵提升效率
        """
        indegrees = {i: 0 for i in range(n)}
        adjacency = [[False] * n for _ in range(n)]
                
        # 统计入度
        for road in roads:
            u, v = road
            indegrees[u] += 1
            indegrees[v] += 1
            adjacency[u][v] = True
            adjacency[v][u] = True
        
        # 降序排
        sorted_indegrees = sorted(indegrees.items(), key=lambda x: x[1], reverse=True)
        
        # 查找最大网络排名
        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                u, v = sorted_indegrees[i][0], sorted_indegrees[j][0]
                if indegrees[u] + indegrees[v] < max_rank:
                    # 如果当前组合的最大可能值已经小于max_rank，提前退出循环
                    break
                rank = indegrees[u] + indegrees[v]
                if adjacency[u][v]:
                    rank -= 1
                max_rank = max(max_rank, rank)
        
        return max_rank
        