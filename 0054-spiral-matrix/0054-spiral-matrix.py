class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 左，下，右，上
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        length = len(matrix) * len(matrix[0])
        res = [0] * length
        visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        
        # 按照direction的顺序来
        i, j, d = 0, 0, 0
        for k in range(length):
            res[k] = matrix[i][j]
            visited[i][j] = True
            
            dx, dy = directions[d]
            ni, nj = i + dx, j + dy
            
            if ni < 0 or ni >= len(matrix) or nj < 0 or nj >= len(matrix[0]) or visited[ni][nj]:
                d = (d + 1) % 4
                dx, dy = directions[d]
                ni, nj = i + dx, j + dy
            
            i, j = ni, nj
        
        return res