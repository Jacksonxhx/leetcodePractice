class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        二分查找每行的第一位数，找到在哪行
        然后继续二分找在哪个位置
        '''
        if not matrix or not matrix[0]:
            return False
        
        # 二分找在哪行
        l, r = 0, len(matrix) - 1
        # l < r 而不是 l <= r是因为当l == r是我们可以单独check这种情况，会更清楚
        while l < r:
            mid = (l + r) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        # 处理特殊情况并确定在哪一行，因为当l == r时，可能在原有的后面一行
        potential_row = l if l < len(matrix) and matrix[l][0] <= target else l - 1
        if potential_row < 0:
            return False
        
        # 二分找在potential_row中的哪一个
        left, right = 0, len(matrix[potential_row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[potential_row][mid] == target:
                return True
            # 如果 matrix[potential_row][mid] 小于目标值，则在 [mid + 1, right] 中继续搜索
            elif matrix[potential_row][mid] < target:
                left = mid + 1
            # 如果 matrix[potential_row][mid] 大于目标值，则在 [left, mid - 1] 中继续搜索
            else:
                right = mid - 1
        
        return False