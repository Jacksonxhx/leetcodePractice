class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        遍历所有node，每个遍历四周
        """
        directions = {(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)}
        rows = len(board)
        cols = len(board[0])
        
        for row in range(rows):
            for col in range(cols):
                live = 0
                for dx, dy in directions:
                    nx, ny = row + dx, col + dy
                    if 0 <= nx < rows and 0 <= ny < cols and abs(board[nx][ny]) == 1:
                        live += 1
                    
                if board[row][col] == 1:
                    if live < 2 or live > 3:
                        board[row][col] = -1
                    else:
                        continue      

                elif board[row][col] == 0 and live == 3:
                    board[row][col] = 2
        
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == -1:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1
        