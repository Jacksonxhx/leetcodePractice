from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        '''
        先统计有多少个1，然后遍历在boundary上的1，用visited记录
        '''
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        queue = deque()
        
        # 统计有多少个1
        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # 加入所有在boundary的1
                    if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                        queue.append((i, j))
                    
                    cnt += 1
    
        # 用bfs找
        while queue:
            i, j = queue.pop()
            
            if visited[i][j]:
                continue
            
            visited[i][j] = True
            cnt -= 1
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny))
        
        return cnt