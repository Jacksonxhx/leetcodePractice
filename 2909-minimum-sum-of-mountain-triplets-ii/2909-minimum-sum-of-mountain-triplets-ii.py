class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        """
        用prefix和suffix做
        """
        n = len(nums)
        if n < 3:
            return -1
        
        # prefix_min[i] = min(nums[0], nums[1], ..., nums[i])
        prefix_min = [float('inf')] * n
        # suffix_min[i] = min(nums[i], nums[i + 1], ..., nums[n - 1])
        suffix_min = [float('inf')] * n
        
        prefix_min[0] = nums[0]
        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i - 1], nums[i])
            
        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])
        
        res = float('inf')
        for j in range(1, n - 1):
            if prefix_min[j - 1] < nums[j] and suffix_min[j + 1] < nums[j]:
                res = min(res, prefix_min[j - 1] + nums[j] + suffix_min[j + 1])
        
        return res if res != float('inf') else -1