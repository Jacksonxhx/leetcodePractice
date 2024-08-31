class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        # 针对每个circle，找到左min和右max，然后go through所有的integer point
        # 加入set查看
        res = set()
        
        for i in range(len(circles)):
            x, y, r = circles[i][0], circles[i][1], circles[i][2]
            min_x = math.ceil(x - r)
            min_y = math.ceil(y - r)
            max_x = math.floor(x + r)
            max_y = math.floor(y + r)
            
            for j in range(min_x, max_x + 1):
                for k in range(min_y, max_y + 1):
                    if (x - j) ** 2 + (y - k) ** 2 <= r ** 2:
                        res.add((j, k))
        
        return len(res)
            