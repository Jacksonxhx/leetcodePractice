from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        从每个1开始搜如果四周有1step不用加，没有的话step ++
        BFS做，无权边，用BFS做最短路，本质就是一个岛到另一个岛的最短路
        首先把第一次遇到的一个岛屿做标记，变成-1
        """
        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] != 1:
                return
            # 标记岛屿
            grid[x][y] = -1
            # 把标记岛屿加入queue为后面bfs作准备
            queue.append((x, y))
            for dx, dy in directions:
                dfs(x + dx, y + dy)
            
            
        # 方向：上下左右
        directions = [(-1, 0), (1, 0), (0,-1), (0, 1)]
        n = len(grid)
        queue = deque()
        
        # 给第一个岛做标记，用dfs
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
        
        # 用BFS，寻找最短路径到第二个岛屿
        steps = 0
        while queue:
            # 每一层
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            # BFS第一次找到的一定是最短
                            return steps
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = -1
                            queue.append((nx, ny))
            steps += 1
            
        return -1