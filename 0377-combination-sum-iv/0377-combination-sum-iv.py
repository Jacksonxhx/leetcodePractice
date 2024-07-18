class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n, m = len(nums), target
        
        # dp含义：当前容量下，最多可以有多少种组合方法
        dp = [0] * (m + 1)
        # 凑0有1种
        dp[0] = 1
        
        # 遍历所有可能的容量
        for i in range(m + 1):
            # 每个容量判断nums的值会不会大于容量
            for j in range(1, n + 1):
                # 判断，如果不大于，加入
                if i >= nums[j - 1]:
                    dp[i] = dp[i] + dp[i - nums[j - 1]] 
        
        return dp[m]