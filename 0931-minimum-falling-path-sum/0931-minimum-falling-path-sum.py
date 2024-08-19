class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # 假设从r，c出发，从下往上出发
        # 可以写出状态转移方程：dfs(r, c) = min(dfs(r - 1, c - 1), dfs(r - 1, c), dfs(r - 1, c + 1)) + matrix[r][c]
        # 确定递归的边界dfs(0, c) = matrix[0][c]，出界不合法，设置成无穷大
        n = len(matrix)

        # dfs(r, c)表示从 matrix[r][c] 出发，向上走到第一行的最小路径和
        @cache
        def dfs(r: int, c:int) -> int:
            # 出界
            if c < 0 or c >= n:
                return inf
            # 到达第一行
            if r == 0:
                return matrix[0][c]

            return min(dfs(r - 1, c- 1), dfs(r - 1, c), dfs(r - 1, c + 1)) + matrix[r][c]

        # 依次遍历最后一排的每个位子
        return min(dfs(n - 1, i) for i in range(n))