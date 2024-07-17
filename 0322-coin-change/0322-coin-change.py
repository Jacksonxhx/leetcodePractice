class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n, m = len(coins), amount
        # 这里v，w就是coins
        
        # dp含义：背包装了i的时候的最小的数量
        dp = [m + 1] * (m + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for j in range(coins[i - 1], m + 1):
                dp[j] = min(dp[j], dp[j - coins[i - 1]] + 1)
                
        if dp[m] != m + 1:
            return dp[m]
        return -1
        