from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        BFS和队列做，核心思路是所有2橘子是一层，继续往下找
        '''
        
        # 初始化
        queue = deque()
        fresh_oranges = 0
        
        # 遍历网格，初始化队列和新鲜橙子计数
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        # 如果没有新鲜橙子，直接返回0
        if fresh_oranges == 0:
            return 0
        
        # 计数和方向
        minute = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # BFS
        while queue:
            minute += 1
            # 遍历一层的
            for _ in range(len(queue)):
                # 取第一个
                x, y = queue.popleft()
                for dx, dy in directions:
                    # 上下左右找新的
                    nx, ny = x + dx, y + dy
                    # 判断
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh_oranges -= 1
            
            # 当所有的好橘子都变了后
            if fresh_oranges == 0:
                return minute
            
        return -1