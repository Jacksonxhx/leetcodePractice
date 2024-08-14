from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        n = len(nums)
        _max, _max_freq = 0, 0
        for key, value in cnt.items():
            if value > _max_freq:
                _max = key
                _max_freq = value
        
        # 记录前半max的数量
        _half_max = 0
        
        for i in range(n - 1):
            if nums[i] == _max:
                _half_max += 1
            
            if _half_max * 2 > (i + 1) and (_max_freq - _half_max) * 2 > (n - i - 1):
                return i
        
        return -1