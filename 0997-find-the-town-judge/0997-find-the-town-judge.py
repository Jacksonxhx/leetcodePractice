class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        judge的入度为n-1，出度为0
        """
        if n == 1:
            return 1 if not trust else -1
        
        # 初始化入度和出度
        indegrees = [0] * (n + 1)
        outdegrees = [0] * (n + 1)
        
        # 计算出度入度
        for a, b in trust:
            outdegrees[a] += 1
            indegrees[b] += 1
        
        # 找judge
        for i in range(1, n + 1):
            if indegrees[i] == n - 1 and outdegrees[i] == 0:
                return i
        
        return -1