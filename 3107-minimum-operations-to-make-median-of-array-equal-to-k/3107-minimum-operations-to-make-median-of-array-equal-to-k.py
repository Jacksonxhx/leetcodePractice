class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        # 首先排序，然后把median左边所有大于k的变成k，右边小于k的变成k
        nums = sorted(nums)
        n = len(nums)
        # 因为even取上面
        middle = n // 2
        
        res = 0
        for i in range(n):
            if i < middle and nums[i] > k:
                res += nums[i] - k
            elif i == middle and nums[i] != k:
                res += abs(nums[i] - k)
            elif i > middle and nums[i] < k:
                res += k - nums[i]
        
        return res
        