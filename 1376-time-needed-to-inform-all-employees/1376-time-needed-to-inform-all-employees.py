from collections import deque

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """
        用BFS，按树的结构，total inform time就是所有层的inform time的最大值之和
        """
        # 每一位的subordinate
        graph = {i: [] for i in range(n)}
        for i in range(n):
            if manager[i] != -1:
                graph[manager[i]].append(i)
            
        # 定义queue，append元组，id和time
        queue = collections.deque([(headID, 0)])
        max_t = 0        
    
        # BFS
        while queue:
            u, c_t = queue.popleft()
            max_t = max(max_t, c_t)
            
            for sub in graph[u]:
                queue.append((sub, c_t + informTime[u]))
        
        return max_t