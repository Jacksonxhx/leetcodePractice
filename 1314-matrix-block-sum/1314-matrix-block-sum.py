class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """
        1 2 3 4四个角，4 = 2 + 3 - 1
        """
        m, n = len(mat), len(mat[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = mat[i][j] + dp[i + 1][j] + dp[i][j + 1] - dp[i][j]
        
        res = [[0] * n for _ in range(m)]
        
        # 计算结果
        for i in range(m):
            for j in range(n):
                # 确定边界
                r1 = max(0, i - k)
                r2 = min(m, i + k + 1)
                c1 = max(0, j - k)
                c2 = min(n, j + k + 1)
                
                # 和 = 4 - 2 - 3 + 1
                res[i][j] = dp[r2][c2] - dp[r1][c2] - dp[r2][c1] + dp[r1][c1]
        
        return res