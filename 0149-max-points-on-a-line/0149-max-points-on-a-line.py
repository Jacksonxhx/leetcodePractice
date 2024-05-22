class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        '''
        斜率一样，把斜率当作key
        统计所有的点和别的点组成的斜率，记住如果斜率相同，这个点pass掉不再记录
        需要处理很多边界情况，dx，dy不同号，垂直平行等情况
        '''
        n = len(points)
        if n < 3:
            return n
        ans = 0
        for i in range(n):
            line_dict = dict()
            line_dict[0] = 0
            
            # 从当前点的下一个开始遍历
            for j in range(i+1, n):
                # x，y方向的改变量
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                # 通过用gcd去处理所有dx，dy的情况，让他们最小
                # 不会出现浮点数不同的情况
                gcd_dx_dy = math.gcd(abs(dx), abs(dy))
                # 同号
                if (dx > 0 and dy > 0) or (dx < 0 and dy < 0):
                    dx = abs(dx) // gcd_dx_dy
                    dy = abs(dy) // gcd_dx_dy
                # 异号
                elif dx < 0 and dy > 0:
                    dx = -dx // gcd_dx_dy
                    dy = -dy // gcd_dx_dy
                # 异号
                elif dx > 0 and dy < 0:
                    dx = dx // gcd_dx_dy
                    dy = dy // gcd_dx_dy
                # 垂直或平行
                elif dx == 0 and dy != 0:
                    dy = 1
                elif dx != 0 and dy == 0:
                    dx = 1
                
                # 设置key
                key = (dx, dy)
                if key in line_dict:
                    line_dict[key] += 1
                else:
                    line_dict[key] = 1
                    
            ans = max(ans, 1 + max(line_dict.values()))
        return ans