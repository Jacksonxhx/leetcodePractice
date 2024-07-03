class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        str_n = bin(n)[2:]
        res = 0
        for ch in str_n:
            if ch == '1':
                res += 1
        
        return res == 1