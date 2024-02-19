class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        # 使用key为x[0]作为指标进行排序
        intervals.sort(key=lambda x:x[0])
        
        merged = []
        
        # 遍历一遍所有intervals
        for interval in intervals:
            # 如果merged是空 or merge中最大的一个interval的close value小于下一个interval的start
            # 这里必须是 < 而不是 <= 不然的话会重复
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
    
    # 相当于只需要关注new interval的范围，范围内的可以直接不管