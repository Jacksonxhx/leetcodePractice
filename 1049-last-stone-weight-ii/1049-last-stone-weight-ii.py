class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        可以转换了01背包，相当于找最小的两个subset和之差
        """
        # 因为len <= 30 and stone[i] <= 100, 所以一半的sum max == 1500
        n, m = len(stones), 1500
        
        # 将石头放在j容量的背包最大价值
        dp = [0] * (m + 1)
        
        # 这里是stones一半的
        target = sum(stones) // 2
        
        # 这里v = w = stones
        for i in range(1, n + 1):
            for j in range(target, stones[i - 1] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i - 1]] + stones[i - 1])
        
        return sum(stones) - 2 * dp[target]