class Solution:
    def __init__(self):
        self.res = 0
    
    def backtrack(self, chessboard, row, n):
        if row == n:
            self.res += 1
            return
        
        # 递归每一行的每一列
        for col in range(n):
            if self.isValid(chessboard, n, row ,col):
                chessboard[row][col] = 'Q'
                self.backtrack(chessboard, row + 1, n)
                chessboard[row][col] = '.'
        
    def isValid(self, chessboard, n, row, col) -> bool:
        
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False
        
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False 
            
            i -= 1
            j -= 1
        
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if chessboard[i][j] == 'Q':
                return False 
            
            i -= 1
            j += 1
        
        return True
    
    def totalNQueens(self, n: int) -> int:
        # 按照每行来判断是否要放Q
        chessboard = [['.' for _ in range(n)] for _ in range(n)]
        self.backtrack(chessboard, 0, n)
        return self.res