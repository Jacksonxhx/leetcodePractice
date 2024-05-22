class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        其实就是无向图找scc找有几个，可以用dfs做
        一个scc就是一座岛
        
        方法就是每到一个1，就更新上下左右的位置，如果是1就call recursion
        然后把邻近的1都变成0，这样就可以找到一个scc
        所以最后触发了几次dfs就有几个岛
        '''
        count = 0
        
        # 遍历一遍grid，遇到'1'的话遍历dfs
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        
        return count 
        
    def dfs(self, grid, i, j):
        n = len(grid)
        m = len(grid[0])
        # 处理grid[i][j]是'0'的情况，直接return
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == '0':
            return 0
        # 把grid[i][j] '1'变成'0'
        grid[i][j] = '0'
        # recursion call继续处理四周的情况
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        
        