class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        '''
        用公式Brian Kernigham的n & (n - 1)算，这会清除了n最右边的1
        相当于每两个数有公共前缀，长度为x，所以a和b的x+1位是0和1
        所以用n&(n-1)可以把x+1位变成0，所以从right开始清除到left就求了最后的解
        '''
        while left < right:
            right = right & (right - 1)
        return right 