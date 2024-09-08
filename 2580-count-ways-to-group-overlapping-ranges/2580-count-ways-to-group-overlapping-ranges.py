class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        # 先sort然后merge
        ranges.sort()
        new_ranges = []
        
        # 初始化起始区间
        start, end = ranges[0]
        
        for i in range(1, len(ranges)):
            # 如果重叠，更新end
            if ranges[i][0] <= end:
                end = max(end, ranges[i][1])
            # 如果不重叠，将之前的区间加入结果，并更新新的开始和结束位置
            else:
                new_ranges.append([start, end])
                start, end = ranges[i]
        
        new_ranges.append([start, end])
        
        MOD = 10**9 + 7
        return pow(2, len(new_ranges), MOD)
