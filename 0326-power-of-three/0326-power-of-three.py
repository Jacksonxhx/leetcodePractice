class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        # 达到Max
        if (3 ** 19) % n == 0:
            return True
        return False