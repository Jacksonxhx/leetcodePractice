from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        BFS做，每个空是一层，然后遍历每个空怎么走，如果上下左右遇到空，就append到queue
        如果遇到上下左右是outside就是出口
        用一个cnt记录
        """
        rows, cols = len(maze), len(maze[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # (x, y, steps)
        queue = deque([(entrance[0], entrance[1], 0)])
        
        # 确保不走重复
        visited = set((entrance[0], entrance[1]))    
        
        while queue:
            x, y, steps = queue.popleft()
            
            # 上下左右
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # 如果是到空地
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == '.':
                    # 如果到了exir
                    if (nx == 0 or ny == 0 or nx == rows - 1 or ny == cols - 1) and [nx, ny] != entrance:
                        return steps + 1
                    # 不然加入visited和queue，同时step ++
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny, steps + 1))
        
        # 没找到返回-1
        return -1