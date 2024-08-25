from collections import deque

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        """
        使用bfs找到(row, col)所在的connected component
        然后边找边判断是不是要变
        """
        n, m = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = [[0 for _ in range(m)] for _ in range(n)]
        visited = set([(row, col)])
        queue = deque([(row, col)])
        
        while queue:
            r, c = queue.popleft()
            is_border = False
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == grid[row][col]:
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                else:
                    is_border = True
            
            if is_border:
                res[r][c] = color
            else:
                res[r][c] = grid[r][c]
        
        # 如果不是边界的格子，将原颜色赋值回去
        for i in range(n):
            for j in range(m):
                if res[i][j] == 0:
                    res[i][j] = grid[i][j]
        
        return res
        
        
        