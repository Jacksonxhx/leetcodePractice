class Solution:
    def numSquares(self, n: int) -> int:
        # dp含义：当值是i的时候的最少的完全平方数
        dp = [n + 1 for _ in range(n + 1)]
        # 凑0不需要值
        dp[0] = 0
        
        # 最多只有不超过向下取整sqrt(n)个数，因为是平方数
        for i in range(1, int(sqrt(n)) + 1):
            # 这个就是v[i]，n + 1是背包容量
            num = i * i
            for j in range(num, n + 1):
                dp[j] = min(dp[j], dp[j - num] + 1)
        
        # 最后判断一下
        if dp[n] != n + 1:
            return dp[n]
        return -1