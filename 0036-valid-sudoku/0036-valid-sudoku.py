class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_unit(unit):
            seen = set()
            for num in unit:
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)
            return True
        
        # 检查每一行
        for row in board:
            if not is_valid_unit(row):
                return False

        # 检查每一列
        for col in zip(*board):
            if not is_valid_unit(col):
                return False
        
        # 检查3x3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not is_valid_unit(subgrid):
                    return False

        return True