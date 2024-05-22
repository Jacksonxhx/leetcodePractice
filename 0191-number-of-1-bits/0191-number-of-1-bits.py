class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 1
        
        while n != 1:
            if n % 2 != 0:
                n //= 2
                res += 1
            else:
                n //= 2
        
        return res