class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        """
        prefix sum
        """
        m, n = len(grid), len(grid[0])
        res = 0
        # prefix[i + 1][j + 1]:grid[0:i][0:j]之和
        prefix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        # 构建prefix     
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                prefix[i + 1][j + 1] = prefix[i + 1][j] + prefix[i][j + 1] - prefix[i][j] + x
                if prefix[i + 1][j + 1] <= k:
                    res += 1
        
        return res