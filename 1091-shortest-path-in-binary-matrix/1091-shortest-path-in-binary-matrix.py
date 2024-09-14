from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        用bfs，8个方向
        """
        if grid[0][0] == 1:
            return -1
        
        n = len(grid)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        res = 0
        queue = deque([(0, 0)])
        visited = set((0, 0))
        
        while queue:
            res += 1
            
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                if x == y == n - 1:
                    return res
            
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) not in visited and 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
        
        return -1