class Solution:
    def judge(self, weight, value, m):
        n = len(weight)
        dp = [0 for _ in range(m + 1)]
        
        for i in range(1, n + 1):
            for j in range(m, weight[i - 1] - 1, -1):
                dp[j] = max(dp[j], dp[j - weight[i - 1]] + value[i - 1])
        
        return dp[m]
    
    
    
    def canPartition(self, nums: List[int]) -> bool:
        """
        01 背包问题，就是说找到一个子集的和是整个nums的和的一半
        """
        sum_nums = sum(nums)
        if sum_nums & 1:
            return False
        
        target = sum_nums // 2
        return self.judge(nums, nums, target) == target
        