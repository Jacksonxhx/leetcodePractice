class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """
        用二分
        """
        l, r = 1, max(nums)
        while l < r:
            mid = (l + r) // 2
            _sum = sum(math.ceil(num / mid) for num in nums)
            if _sum > threshold:
                l = mid + 1
            else:
                r = mid
                
        return l