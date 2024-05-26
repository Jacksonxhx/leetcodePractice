class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        max_sum = window
        
        for i in range(k, len(nums)):
            window = window + nums[i] - nums[i - k]
            max_sum = max(window, max_sum)
        
        return max_sum / k