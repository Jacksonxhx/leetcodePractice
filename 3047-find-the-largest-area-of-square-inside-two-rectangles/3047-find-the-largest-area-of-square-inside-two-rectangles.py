class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        # 先暴力搜索出所有intersection，然后找max
        res = 0
        n = len(bottomLeft)
        
        for i in range(n):
            for j in range(i + 1, n):
                # 计算相交区域的左下角和右上角
                x_left = max(bottomLeft[i][0], bottomLeft[j][0])
                y_bottom = max(bottomLeft[i][1], bottomLeft[j][1])
                x_right = min(topRight[i][0], topRight[j][0])
                y_top = min(topRight[i][1], topRight[j][1])
                
                # 判断是否有相交区域
                if x_left < x_right and y_bottom < y_top:
                    # 最大正方形的边长为相交区域的宽度和高度的最小值
                    side_length = min(x_right - x_left, y_top - y_bottom)
                    res = max(res, side_length * side_length)
        
        return res