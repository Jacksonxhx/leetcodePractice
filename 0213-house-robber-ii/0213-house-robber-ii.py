class Solution:
    def helper(self, nums):
        size = len(nums)
        
        # dp[i]：前i个房子能偷到的最大金额
        dp = [0] * (size + 1)
        dp[0] = 0
        dp[1] = nums[0]
        
        for i in range(2, size + 1):
            # 取当前的或者不取
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        
        return dp[size]
        
    
    def rob(self, nums: List[int]) -> int:
        """
        转换为[0, size - 2], [1, size - 1]，就和原本一样
        求这两种情况下的最大值，find max
        """
        size = len(nums)
        if size == 1:
            return nums[0]
        
        max_1 = self.helper(nums[0:size - 1])
        max_2 = self.helper(nums[1:size])
        
        return max(max_1, max_2)
        
        