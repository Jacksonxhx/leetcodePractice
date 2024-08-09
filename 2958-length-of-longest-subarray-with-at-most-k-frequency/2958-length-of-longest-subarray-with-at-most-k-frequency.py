class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        滑动窗口+hash
        """
        i, hasht = 0, dict()
        res = 0
        
        for j in range(len(nums)):
            if nums[j] not in hasht:
                hasht[nums[j]] = 1
            else:
                hasht[nums[j]] += 1
                
            while hasht[nums[j]] > k:
                hasht[nums[i]] -= 1
                i += 1
            
            res = max(res, j - i + 1)
            
        return res