class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        '''
        双指针+哈希表优化
        使用哈希表来维护窗口内元素的频次，从而快速判断是否有至少 m 个不同的元素
        '''
        n = len(nums)
        if n < m:
            return 0
        
        freq = defaultdict(int)
        distinct_count = 0
        window_sum = 0
        res = float("-inf")
        
        for i in range(n):
            # add sum and freq
            window_sum += nums[i]
            freq[nums[i]] += 1
            
            # if distinct
            if freq[nums[i]] == 1:
                distinct_count += 1
            
            # window size exceed k
            if i >= k:
                window_sum -= nums[i - k]
                freq[nums[i - k]] -= 1
                
                if freq[nums[i - k]] == 0:
                    distinct_count -= 1
            
            if i >= k - 1 and distinct_count >= m:
                res = max(res, window_sum)
        
        return res if res != float("-inf") else 0
        