class Solution:
    def smallestValue(self, n: int) -> int:
        """
        设计是从小到大找因数，重复除，所以不需要判断因数是否是质数
        """
        while True:
            # x是更新的n，s是质因数的和，i是因数
            x, s, i = n, 0, 2
            # 因为是质因数，i * i > x就不可能是因数了
            while i * i <= x:
                # 当x能被i整除的时候，确保了因数都是质数
                while x % i == 0:
                    # sum += i
                    s += i
                    # 更新x
                    x //= i
                i += 1
            if x > 1: s += x
            # n是质数了
            if s == n: return n
            n = s