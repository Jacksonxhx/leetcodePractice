class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        if sum(nums) == 0:
            return 0
        
        tmp = []
        for i in range(len(nums)):
            if nums[i] == 1:
                tmp.append(i)
        
        res = 1
        for i in range(1, len(tmp)):
            res *= tmp[i] - tmp[i - 1]
            res %= 10 ** 9 + 7
        
        return res