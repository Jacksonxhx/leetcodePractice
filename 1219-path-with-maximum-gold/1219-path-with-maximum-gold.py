class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # 用回溯
        self.max_gold = 0
        self.cur_gold = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def backtrack(row, col):
            # 遇到0结束
            if grid[row][col] == 0:
                return
            
            gold = grid[row][col]
            
            self.cur_gold += gold
            self.max_gold = max(self.max_gold, self.cur_gold)
            
            # 走过了
            grid[row][col] = 0
            
            for nx, ny in directions:
                dx, dy = row + nx, col + ny
                if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]):
                    backtrack(dx, dy)
            
            # backtrack
            self.cur_gold -= gold
            grid[row][col] = gold 
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                backtrack(row, col)
		
        return self.max_gold