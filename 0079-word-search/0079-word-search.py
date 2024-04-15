class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        使用回溯算法在二维矩阵中按照上下左右四个方向递归搜索
        backtracking(i, j, index): 表示从board[i][j]出发，能否搜索到单词字母word[index] -> bool
        """
        # 定义四个方向
        directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(board)
        if rows == 0:
            return False
        cols = len(board[0])
        # 定义一个visited数组表示状态
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        def backtracking(i, j, index) -> bool:
            # 当遍历到最后一位的时候，直接return下一个位子，不需要new i j
            if index == len(word) - 1:
                return board[i][j] == word[index]
            
            # 当进入回溯，先判断当前是否一样，如果一样进入探索
            if board[i][j] == word[index]:
                # 首先更新当前的点visited状态
                visited[i][j] = True
                # 遍历四个方向
                for direct in directs:
                    new_i = i + direct[0]
                    new_j = j + direct[1]
                    # 设置好边界和状态确保不重复
                    if 0 <= new_i < rows and 0 <= new_j < cols and visited[new_i][new_j] == False:
                        # recursion
                        if backtracking(new_i, new_j, index + 1):
                            return True
                # 回溯
                visited[i][j] = False
            return False
        
        # 程序开始，遍历每行每列所有的内容，当找到，return
        for i in range(rows):
            for j in range(cols):
                if backtracking(i, j, 0):
                    return True
                
        return False