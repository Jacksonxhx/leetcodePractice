class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        用二分查找找到对应的值
        '''
        if x < 2:
            return x
        
        # 因为任何大于 1 的数的平方根不可能大于其一半
        left, right = 2, x // 2
        
        while left <= right:
            mid = (left + right) // 2
            num = mid * mid
            
            if num == x:
                return mid
            elif num < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right