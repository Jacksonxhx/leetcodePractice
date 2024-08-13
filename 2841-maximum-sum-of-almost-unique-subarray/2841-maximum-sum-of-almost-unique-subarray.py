class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        '''
        双指针+哈希表优化
        使用哈希表来维护窗口内元素的频次，从而快速判断是否有至少 m 个不同的元素
        '''
        n = len(nums)
        if k > n:  
            return 0
        
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i-1] + nums[i - 1]
        
        i, j = 0, k
        res = float("-inf")
        
        while j <= n:
            if len(set(nums[i:j])) >= m:
                res = max(res, prefix[j] - prefix[i])
            i += 1
            j = i + k
        
        return res if res != float("-inf") else 0
        