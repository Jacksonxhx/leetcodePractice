class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # 假设最大能拿到的糖为i，所以[0,i]之间都能被拿，具有二分性
        # 判断每个小孩分到i个糖果的时候是否能满足需求
        def check(i: int) -> bool:
            res = 0
            for c in candies:
                res += c // i
            return res >= k
        
        # 二分，上线是max(candies) + 1
        l, r = 1, max(candies) + 1

        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid
        
        return l - 1
        