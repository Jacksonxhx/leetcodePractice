class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        用prefix
        """
        res = [0] * (n + 1)
        
        for i, j, k in bookings:
            # 之后再loop一遍就能实现prefix
            res[i - 1] += k
            res[j] -= k
        
        for i in range(1, n):
            res[i] += res[i - 1]
        
        return res[:-1]