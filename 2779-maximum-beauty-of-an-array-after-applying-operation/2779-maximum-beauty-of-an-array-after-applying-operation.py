class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        res = 0
        
        for j in range(n):
            while nums[j] - nums[i] > 2 * k:
                i += 1
            
            res = max(res, j - i + 1)
        
        return res