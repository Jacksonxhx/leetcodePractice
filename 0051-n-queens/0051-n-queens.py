class Solution:
    def __init__(self): 
        self.res = []
        
    # 放Q在第几行
    def backtrack(self, chessboard, row, n):
        # 放最后一行
        if row == n:
            tmp_res = []
            for tmp in chessboard:
                tmp_str = ''.join(tmp)
                tmp_res.append(tmp_str)
            self.res.append(tmp_res)
            return
        
        for col in range(n):
            # 如果插入这个位置是合理的
            if self.isValid(n, row, col, chessboard):
                # 更新位置
                chessboard[row][col] = 'Q'
                # 检查下一行
                self.backtrack(chessboard, row + 1, n)
                # 回溯
                chessboard[row][col] = '.'
    
    # util check 函数
    def isValid(self, n, row, col, chessboard):
        # 检查这一列有没有Q
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False
            
        i, j = row - 1, col - 1
        # 检查左对角线
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False
            
            i -= 1
            j -= 1
        
        i, j = row - 1, col + 1
        # 检查右对角线
        while i >= 0 and j < n:
            if chessboard[i][j] == 'Q':
                return False
            
            i -= 1
            j += 1
        
        return True
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res.clear()
        chessboard = [['.' for _ in range(n)] for _ in range(n)]
        self.backtrack(chessboard, 0, n)
        return self.res