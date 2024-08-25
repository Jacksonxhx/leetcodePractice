class Solution:
    def countCollisions(self, directions: str) -> int:
        # 去掉左边往左，右边往右的
        directions = directions.lstrip("L").rstrip("R")
        
        collision = 0
        
        for d in directions:
            if d != 'S':
                collision += 1
        
        return collision