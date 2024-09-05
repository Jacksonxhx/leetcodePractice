from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # j - i != nums[j] - nums[i]就是nums[i] - i != nums[j] - j
        hasht = defaultdict(int)
        for i in range(len(nums)):
            tmp = nums[i] - i
            hasht[tmp] += 1
        
        n = len(nums)
        res = 0
        for i in range(1, n):
            res += i
        
        for key, value in hasht.items():
            if value > 1:
                for i in range(1, value):
                    res -= i
        
        return res
        