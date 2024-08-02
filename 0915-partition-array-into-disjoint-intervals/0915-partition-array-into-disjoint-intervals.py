class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        """
        先记录每个位子上，最大的nums，从后往前，然后从前往后判断找到分界点
        """
        n = len(nums)
        min_r = [0] * n
        min_r[n - 1] =  nums[n - 1]
        for i in range(n -2, -1, -1):
            min_r[i] =  min(nums[i], min_r[i + 1])
        
        max_l = nums[0]
        for i in range(1, n):
            if max_l <= min_r[i]:
                return i
            max_l = max(max_l, nums[i])