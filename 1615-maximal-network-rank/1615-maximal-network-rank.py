class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        """
        找最大的的入度pair
        找到之后判断是否相连，如果相链 max--
        """
        indegrees = {i: 0 for i in range(n)}
        
        # 统计入度
        for road in roads:
            indegrees[road[0]] += 1
            indegrees[road[1]] += 1
        
        # 降序排
        sorted_indegrees = sorted(indegrees.items(), key=lambda x: x[1], reverse=True)
        
        # 查找最大网络排名
        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                u, v = sorted_indegrees[i][0], sorted_indegrees[j][0]
                rank = sorted_indegrees[i][1] + sorted_indegrees[j][1]
                if [u, v] in roads or [v, u] in roads:
                    rank -= 1
                max_rank = max(max_rank, rank)
        
        return max_rank
        