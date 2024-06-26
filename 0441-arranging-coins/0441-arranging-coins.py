class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        用二分，总数是total 
        """
        l, r = 1, n
        
        while l <= r:
            mid = (l + r) // 2
            # 前 mid 行的硬币总数
            total = mid * (mid + 1) // 2
            
            if total == n:
                return mid
            elif total < n:
                l = mid + 1
            else:
                r = mid - 1
        
        # r是最大的可能性
        return r