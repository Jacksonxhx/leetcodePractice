import collections

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        """
        创建一个按照开头排序的tuple(start, i)
        然后对于每个区间使用二分查找，使得在有序的区间起点列表中找到第一个起点大于或等于该区间终点的区间
        所以相当于是在一个构建好的start里找第一个比当前end大的start
        """
        n = len(intervals)
        if n == 0:
            return []
        
        # 按照start排序
        sorted_intervals = sorted((interval[0], i) for i, interval in enumerate(intervals))
        res = []
        
        # 使用二分查找找到第一个start大于当前区间end的值
        def binary_search(sorted_intervals, target):
            # r == len(sorted_intervals)是为了判断是否存在
            l, r = 0, len(sorted_intervals)
            
            while l < r:
                mid = (l + r) // 2
                if sorted_intervals[mid][0] >= target:
                    r = mid
                else:
                    l = mid + 1
            return l
        
        # 查找每个interval
        for interval in intervals:
            idx = binary_search(sorted_intervals, interval[1])
            if idx < n:
                res.append(sorted_intervals[idx][1])
            else:
                res.append(-1)
        
        return res