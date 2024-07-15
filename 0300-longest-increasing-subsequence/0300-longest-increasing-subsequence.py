class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [1] * size
        
        for i in range(size):
            # 遍历i之前的
            for j in range(i):
                if nums[i] > nums[j]:
                    # 状态转移是要更新之前的位置的max
                    dp[i] = max(dp[i], dp[j] + 1)
                   
        
        return max(dp)