class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        nums = sorted(nums)
        size = len(nums)
        cnt = 0
        
        # 1 2 4 8 compute 2的次方
        pow2 = [1] * size
        for i in range(1, size):
            pow2[i] = pow2[i-1] * 2 % mod
        
        l, r = 0, size - 1
        while l <= r:
            if nums[l] + nums[r] <= target:
                cnt = (cnt + pow2[r - l]) % mod
                l += 1
            else:
                r -= 1
        
        return cnt % mod
        