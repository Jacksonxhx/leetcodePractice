class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        用dp去考虑
        如果 dp[i-1] 是正数，那么 dp[i] 就等于 dp[i-1] 加上当前的 nums[i]，否则 dp[i] 就等于 nums[i]
        '''  
        size = len(nums)
        # 以第i个数结尾的连续子数组的最大和
        dp = [0] * size
        
        # initialization
        dp[0] = nums[0]
        
        for i in range(1, size):
            if dp[i - 1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]
        return max(dp)
            