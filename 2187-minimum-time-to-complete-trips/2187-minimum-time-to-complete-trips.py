class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # 向下取整看看到现在为止ith位置的bus跑了几次
        def trips_in_time(t: int) -> int:
            return sum(t // t_i for t_i in time)
        
        # right表示最大的可能时间，最快公车*totalTrips
        left, right = 1, min(time) * totalTrips
        
        while left < right:
            mid = (left + right) // 2
            if trips_in_time(mid) >= totalTrips:
                right = mid
            else:
                left = mid + 1
        
        return left
        
        