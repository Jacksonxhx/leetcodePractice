class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        """
        先构建odd even prefix
        然后算去掉index之后的sum O(1)
        """
        n = len(nums)
        odd_prefix, even_prefix = [0] * (n + 1), [0] * (n + 1)
        for i, num in enumerate(nums):
            odd_prefix[i] += odd_prefix[i - 1]
            even_prefix[i] += even_prefix[i - 1]
            
            if i % 2 == 0:
                odd_prefix[i] += num
            else:
                even_prefix[i] += num
        
        res = 0
        for i, num in enumerate(nums):
            even_after_removed = even_prefix[i-1] + odd_prefix[n-1] - odd_prefix[i]
            odd_after_removed = odd_prefix[i-1] + even_prefix[n-1] - even_prefix[i]
            res += (even_after_removed == odd_after_removed)
        return res