class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        """
        用dfs遍历每个group找最大最小xy
        """
        def dfs(x, y):
            stack = [(x, y)]
            # 将当前格子标记为已访问
            land[x][y] = 0 
            min_x, min_y = x, y
            max_x, max_y = x, y
            
            while stack:
                cur_x, cur_y = stack.pop()
                min_x = min(min_x, cur_x)
                min_y = min(min_y, cur_y)
                max_x = max(max_x, cur_x)
                max_y = max(max_y, cur_y)
                
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
                    nx, ny = cur_x + dx, cur_y + dy
                    if 0 <= nx < len(land) and 0 <= ny < len(land[0]) and land[nx][ny] == 1:
                        stack.append((nx, ny))
                        land[nx][ny] = 0
            
            return [min_x, min_y, max_x, max_y]
        
        res = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    res.append(dfs(i, j))
        
        return res