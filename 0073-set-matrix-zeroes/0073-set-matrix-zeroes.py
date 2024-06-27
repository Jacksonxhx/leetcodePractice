class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        先收集所有0，写一个辅助函数获取该位置横纵轴
        """
        rows, cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()
        
        # 收集所有的0点位置
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        # 将收集到的行置零
        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0
        
        # 将收集到的列置零
        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0
        