from collections import defaultdict

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        # 用matrix[i][j]记录friend i 对 j的感受，O(1)读取
        records = [[-1 for _ in range(n)] for _ in range(n)]
        
        for i, preference in enumerate(preferences):
            for j, p in enumerate(preference):
                records[i][p] = j
        
        res = 0
        # 建图
        partner = [0] * n
        for x, y in pairs:
            partner[x] = y
            partner[y] = x
        
        for x in range(n):
            y = partner[x] 
            for u in preferences[x]:
                if u == y:
                    break  
                v = partner[u] 
                if records[u][x] < records[u][v]:
                    res += 1
                    break  
        return res
                    