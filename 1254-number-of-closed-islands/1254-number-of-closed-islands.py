class Solution:
    def dfs(self, grid, i, j):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        if grid[i][j]:
            return True
        
        # 记录表示来过了
        grid[i][j] = 1
        
        res = True
        for dx, dy in directions:
            nx, ny = i + dx, j + dy
            if not self.dfs(grid, nx, ny):
                res = False
        return res
        
    def closedIsland(self, grid: List[List[int]]) -> int:
        """
        找有几个scc，把在boundary的减掉
        """
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and self.dfs(grid, i, j):
                    res += 1
                    
        return res