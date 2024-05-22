class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            x = 1 / x
            n = -n
        
        # 用recursion吧time complexity变成O(logn)
        def quickPow(x, n):
            if n == 0:
                return 1
            half = quickPow(x, n // 2)
            if n % 2 == 0:
                return half * half
            # 奇数用//就会少乘一个x
            else:
                return half * half * x
            
        return quickPow(x, n)