from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        '''
        先统计有多少个1，然后遍历在boundary上的1，用visited记录
        '''
        rows = len(grid)
        cols = len(grid[0])
        cnt = 0 
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        queue = deque()
        
        # 把所有在boundary的1加入，统计 1 个数
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                        queue.append((row, col))
                                      
                    cnt += 1
        
        tmp = 0
        while queue:
            row, col = queue.popleft()
            if visited[row][col]:
                continue
                
            visited[row][col] = True
            tmp += 1
            
            for dx, dy in directions:
                nx, ny = row + dx, col + dy
                
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny))
         
        return cnt - tmp
            