class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # 使用稳定排序记录ids
        
        # 记录下长度和sum，这样直接减去marked
        n, s = len(nums), sum(nums)
        
        # 按照nums的大小从小到大排序
        ids = sorted(range(n), key=lambda i: nums[i])
        
        res = []
        j = 0
        for i, k in queries:
            s -= nums[i]
            # 标记
            nums[i] = 0 
            while j < n and k:
                i = ids[j]
                # 如果没有被标记
                if nums[i]:
                    s -= nums[i]
                    nums[i] = 0
                    k -= 1
                # 确保不超标
                j += 1
            res.append(s)
            
        return res