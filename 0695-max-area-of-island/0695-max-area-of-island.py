from collections import deque

class Solution:
    def __init__(self):
        self.directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    
    def bfs(self, grid, visited, i, j):        
        queue = deque([(i, j)])
        visited.add((i, j))
        area = 1
        
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1 and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    area += 1
        
        return area
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        visited数组，找scc，存一个max
        """        
        rows = len(grid)
        cols = len(grid[0])
        
        visited = set()
        max_area = 0
        
        for i in range(rows):
            for j in range(cols):
                # 每次遇到一个scc更新一下max area
                if grid[i][j] == 1 and (i, j) not in visited:
                    # area就是一个scc的面积
                    area = self.bfs(grid, visited, i, j)
                    # 更新
                    max_area = max(max_area, area)
        
        return max_area
            
            
        