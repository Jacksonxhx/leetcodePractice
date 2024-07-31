class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        """
        先建图，然后dfs每个non zero cell，算路径之和，return最大
        """
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        start = []
        
        # 统计非0开头
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    start.append((i, j))
        
        res = 0
        visited = set()
        for pair in start:
            if pair in visited:
                continue
            tmp = 0
            stack = [pair]
            while stack:
                r, c = stack.pop()
                tmp += grid[r][c]
                visited.add((r,c))

                for nx, ny in directions:
                    dx, dy = r + nx, c + ny
                    if (dx, dy) not in visited and 0 <= dx < m and 0 <= dy < n and grid[dx][dy] != 0:
                        visited.add((dx, dy))
                        stack.append((dx, dy))
            
            res = max(res, tmp)
        
        return res