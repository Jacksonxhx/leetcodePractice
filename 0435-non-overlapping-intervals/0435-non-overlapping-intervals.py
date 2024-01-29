class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1]) # 使用列表中的每一个参数的第二个数作为排列的key
        end_pos = intervals[0][1] # 最早结束的一个点
        count = 1
        for i in range(1, len(intervals)):
            if end_pos <= intervals[i][0]:
                count += 1
                end_pos = intervals[i][1]
            
        return len(intervals) - count
        
'''
解题思路：

贪心算法：
    把求最少overlapping变成找到最多不overlap
    首先按照结束时间升序排列
    因此会得到距离上次结束时间，最近结束的时段
    如果满足当下，count ++
    最后len-count
'''