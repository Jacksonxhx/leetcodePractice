from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        用BFS去做，通过记录数量来判断
        核心思想就是，所有的2的橘子是一层，然后2往下找，2插入队列
        '''
        fresh_orange = 0
        queue = deque()
        
        # 遍历整个grid，统计fresh_orange和插入2 to queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_orange += 1
                    
        # 如果没有新鲜橙子，直接返回0
        if fresh_orange == 0:
            return 0
        
        # 初始化min记录
        min_pass = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            min_pass += 1
            
            # 进入bfs
            for _ in range(len(queue)):
                x, y = queue.popleft()  
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_orange -= 1
                        queue.append((nx, ny))
            
            # 结束条件
            if fresh_orange == 0:
                return min_pass
            
        return -1
        