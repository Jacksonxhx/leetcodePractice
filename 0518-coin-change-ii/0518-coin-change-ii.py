class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n, m = len(coins), amount
        
        # dp含义：i容量下，最多有几种方案
        dp = [0] * (m + 1)
        # 凑0有1个方案
        dp[0] = 1
        
        for i in range(1, n + 1):
            for j in range(coins[i - 1], m + 1):
                # dp[j] = 使用j和不使用j之和
                dp[j] = dp[j] + dp[j - coins[i - 1]]
        
        return dp[m]
        