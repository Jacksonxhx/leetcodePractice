class Solution:
    def diagonalBinarySearch(self, matrix, diagonal, target):
        left = 0
        right = diagonal
        while left < right:
            mid = (left + right) // 2
            if matrix[mid][mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    
    def rowSearch(self, matrix, begin, cols, target):
        l, r = begin, cols
        while l < r:
            mid = (l + r) // 2
            if matrix[begin][mid] < target:
                l = mid + 1
            elif matrix[begin][mid] > target:
                r = mid - 1
            else:
                l = mid
                break
        
        return begin <= l <= cols and matrix[begin][l] == target
        
    def colSearch(self, matrix, begin, rows, target):
        l = begin - 1
        r = rows
        while l < r:
            mid = (l + r) // 2
            if matrix[mid][begin] < target:
                l = mid + 1
            elif matrix[mid][begin] > target:
                r = mid - 1
            else:
                l = mid
                break
        return begin <= l <= rows and matrix[l][begin] == target
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        if not rows or not cols:
            return False
        
        # 根据diagonal找到行列区域
        min_val = min(rows, cols)
        index = self.diagonalBinarySearch(matrix, min_val - 1, target)
        if matrix[index][index] == target:
            return True
        
        for i in range(index + 1):
            row_search = self.rowSearch(matrix, i, cols - 1, target)
            col_search = self.colSearch(matrix, i, rows - 1, target)
            if row_search or col_search:
                return True
        return False