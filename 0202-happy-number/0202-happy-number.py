class Solution:
    def isHappy(self, n: int) -> bool:
        # 记录第一位，如果循环了输出no
        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.calNumber(n)
            if n == 1:
                return True
        return False
    
    def calNumber(self, m: int) -> int:
        digits = [int(digit) for digit in str(m)]
        res = 0
        for digit in digits:
            res += digit ** 2
        return res
    
    
        
        