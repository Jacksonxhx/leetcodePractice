class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        """
        通过mat存每个数的位置，然后判断
        """
        m, n = len(mat), len(mat[0])
        # 存位置
        index = dict()
        for i in range(m):
            for j in range(n):
                index[mat[i][j]] = (i, j)
        
        row, col = [0] * m, [0] * n
        for k in range(len(arr)):
            # 坐标
            i, j = index[arr[k]]
            row[i] += 1
            col[j] += 1
            if row[i] == n or col[j] == m:
                return k
        
        return -1