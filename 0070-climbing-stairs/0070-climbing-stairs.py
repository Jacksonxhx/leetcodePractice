class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        dp的核心问题就是状态，dp[i] = dp[i- 1] + dp[i - 2]
        需要考虑每一阶的时候，前一阶段有几种可能性，以此往前类推
        '''
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]