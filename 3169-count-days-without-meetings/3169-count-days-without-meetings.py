class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings)
        start, end = 1, 0 
        for s, e in meetings:
            # 不相交
            if s > end:
                # 当前区间长度
                days -= end - start + 1 
                # 更新start
                start = s
            # 维护end
            end = max(end, e)
        # 最后一个合并区间的长度
        days -= end - start + 1
        return days
