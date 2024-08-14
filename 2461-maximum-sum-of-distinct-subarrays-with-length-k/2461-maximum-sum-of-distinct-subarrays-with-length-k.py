class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        用hash存，如果超过1，i++
        """
        hasht = defaultdict(int)
        n = len(nums)
        res, tmp_res = 0, 0
        i, j = 0, 0
        while j < n:
            hasht[nums[j]] += 1
            tmp_res += nums[j]
            
            while j - i + 1 > k or hasht[nums[j]] > 1:
                hasht[nums[i]] -= 1
                tmp_res -= nums[i]
                i += 1
            
            # 当窗口长度等于k并且没有重复元素时，更新结果
            if j - i + 1 == k:
                res = max(res, tmp_res)
            
            # 一直加一
            j += 1
        
        return res