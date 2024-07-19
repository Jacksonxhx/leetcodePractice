class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        def maxInt(a, b):
            if len(a) == len(b):
                return max(a, b)
            if len(a) > len(b):
                return a
            return b
        
        n, m = len(cost), target

        # dp含义: dp[i]就是当cost是i的时候的最大值，str type
        dp = ['#'] * (m + 1)
        dp[0] = ''
        
        for i in range(1, n + 1):
            for j in range(cost[i - 1], m + 1):
                if dp[j - cost[i - 1]] != "#":
                    # dp[j] 就等于不用现在这个和使用现在这个，看哪个更大
                    dp[j] = maxInt(dp[j], str(i) + dp[j - cost[i - 1]])
        
        if dp[m] != '#':
            return dp[m]
        else:
            return "0"