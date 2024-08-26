class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # 使用二维差分处理queries然后计算这个差分矩阵的前缀合
        diff = [[0] * (n + 2) for _ in range(n + 2)]
        for r1, c1, r2, c2 in queries:
            # 从这里开始加
            diff[r1 + 1][c1 + 1] += 1
            # 横向结束
            diff[r1 + 1][c2 + 2] -= 1
            # 纵向结束
            diff[r2 + 2][c1 + 1] -= 1
            # 补一个
            diff[r2 + 2][c2 + 2] += 1
        
        # 根据差分做前缀合
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                diff[i][j] += diff[i][j - 1] + diff[i - 1][j] - diff[i - 1][j - 1]

        # 保留中间
        diff = diff[1:-1]
        for i, row in enumerate(diff):
            diff[i] = row[1:-1]
        return diff