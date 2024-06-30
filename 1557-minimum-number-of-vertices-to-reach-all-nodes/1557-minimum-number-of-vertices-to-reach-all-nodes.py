class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        只需要计算入度为0的node就好
        """
        indegrees = {u: 0 for u in range(n)}
        for edge in edges:
            indegrees[edge[1]] += 1
        
        res = []
        for key, value in indegrees.items():
            if value == 0:
                res.append(key)
        
        return res