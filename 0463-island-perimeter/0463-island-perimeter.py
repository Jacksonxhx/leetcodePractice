from collections import deque

class Solution:
    def bfs(self, grid, rows, cols, row, col):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = collections.deque([(row, col)])

        cnt = 0
        while queue:
            row, col = queue.popleft()
            # visited记录
            grid[row][col] = 2
            # 看四面八方是否是boundary或者水
            for dx, dy in directions:
                nx, ny = row + dx, col + dy
                # 遇到边界或者水域，则周长加 1
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] == 0:
                    cnt += 1
                # 相邻区域为陆地，则将其标记为 2，加入队列
                elif grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    queue.append((nx, ny))
        return cnt
        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        BFS 第一个1，然后四周接壤0或者boundary就cnt ++
        """
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return self.bfs(grid, rows, cols, row, col)
        