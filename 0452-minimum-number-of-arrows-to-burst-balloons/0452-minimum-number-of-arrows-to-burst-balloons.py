class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        贪心：寻找区间重叠最多的地方
        按照points结束的位置升序排列，避免一个range包括了很多小的range
        当坐标小于区间起始位置，count ++
        '''
        if not points:
            return 0
        
        # 按照结束升序排列
        points.sort(key=lambda x: x[1])
        count = 1
        arrow_pos = points[0][1]
        
        for i in range(1, len(points)):
            # 遇到坐标小于区间起始位置
            if points[i][0] > arrow_pos:
                count += 1
                arrow_pos = points[i][1]
        
        return count