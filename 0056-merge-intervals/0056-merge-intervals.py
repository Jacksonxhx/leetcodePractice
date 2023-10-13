class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #处理空集
        if not intervals:
            return []
        #先排好序
        intervals.sort(key=lambda x: x[0]) #根据区间st排序
        #定义开头结尾和答案数组
        st = intervals[0][0]
        ed = intervals[0][1]
        res = []
        #当ed < 当前interval[0]，证明没有交集，append，更新st，ed到当前interval
        #当ed > 当前interval[0]，证明有交集, 更新ed到当前interval[1]
        for interval in intervals:
            if (ed < interval[0]): 
                res.append([st, ed])
                st = interval[0]
                ed = interval[1]
            else: ed = max(ed, interval[1])
        res.append([st, ed])
        return res
        