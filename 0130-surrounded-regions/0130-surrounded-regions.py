class Solution:
    def dfs(self, board, i, j):
        n = len(board)
        m = len(board[0])
        if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != 'O':
            return
        board[i][j] = 'P'
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j - 1)
        self.dfs(board, i + 1, j)
        self.dfs(board, i, j + 1)
            
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        从border开始找'O'，如果找到了变成'P'，是不需要翻的，剩下的'O'全部翻成'X'
        """
        if not board or not board[0]:
            return
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                    self.dfs(board, i, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'P':
                    board[i][j] = 'O'
        
        
        