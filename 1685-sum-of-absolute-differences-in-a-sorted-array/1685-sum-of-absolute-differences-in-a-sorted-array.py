class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """
        use prefix and suffix
        """ 
        n = len(nums)
        # prefix[i]:从0-(i-1)之和
        prefix, suffix = [0] * n, [0] * n
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i + 1]
        
        res = []
        for i in range(n):
            res.append(nums[i] * i - prefix[i] + suffix[i] - nums[i] * (n - i - 1))
        
        return res