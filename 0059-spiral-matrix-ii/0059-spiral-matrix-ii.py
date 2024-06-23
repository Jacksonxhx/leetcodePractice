class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        
        """
        # 左，下，右，上
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = [[0] * n for _ in range(n)]
        
        cnt = 1
        i, j = 0, 0
        d = 0
        while cnt <= n * n:
            res[i][j] = cnt
            cnt += 1
            
            dx, dy = directions[d]
            ni, nj = i + dx, j + dy
            
            if ni < 0 or ni >= n or nj < 0 or nj >= n or res[ni][nj] != 0:
                d = (d + 1) % 4
                dx, dy = directions[d]
                ni, nj = i + dx, j + dy
            
            i, j = ni, nj
        
        return res
        