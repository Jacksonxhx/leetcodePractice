class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        """
        用prefix和suffix
        """
        n = len(nums)
        if n < 3:
            return 0
        
        prefix = [0] * n
        suffix = [0] * n
        
        # 初始化prefix和suffix数组：
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], nums[i])
        
        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = min(suffix[i + 1], nums[i])
        
        res = 0
        for i in range(1, n - 1):
            if prefix[i - 1] < nums[i] < suffix[i + 1]:
                res += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                res += 1
                
        return res