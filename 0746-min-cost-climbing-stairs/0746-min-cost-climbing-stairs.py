class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 最小的cost从位置i爬到top
        n = len(cost)
        dp = [0] * (n + 1)
        
        # n是房顶，从n到n需要0
        dp[n] = 0
        
        # 因为一次只能走1or2步
        # 状态转移方程：dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        # 从n-1开始遍历到0
        for i in range(n - 1, -1, -1):
            # 处理第一步
            if i == n - 1:
                dp[i] = cost[i]  
            else:
                dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        
        return min(dp[0], dp[1])
        
        
        