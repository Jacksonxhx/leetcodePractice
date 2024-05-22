class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        用二分查找找到对应的值
        '''
        left, right = 0, x
        
        while left < right:
            mid = (left + right) // 2
            
            if mid * mid == x or (mid * mid < x and (mid+1) * (mid+1) > x):
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        
        return left