class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # 获取行数和列数
        rows, cols = len(grid), len(grid[0])
        # 方向数组：分别是右上、正右、右下
        directions = [(-1, 1), (0, 1), (1, 1)]
        
        # dfs每个start point
        def dfs(i, j):
            # 该点已经计算过，直接返回
            if (i, j) in memo:
                return memo[(i, j)]
            
            # 初始化最大步数
            max_steps = 0
            
            # 尝试不同方向
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                # 检查边界
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] > grid[i][j]:
                    # dfs回溯
                    max_steps = max(max_steps, dfs(nx, ny) + 1)
            
            # 记录当前max
            memo[(i, j)] = max_steps
            
            return max_steps
        
        # memo 用于保存每个点的最大步数，避免重复计算
        memo = {}
        result = 0
        
        # 从第一列的每个元素开始 DFS
        for i in range(rows):
            result = max(result, dfs(i, 0))
        
        return result
            
            
        