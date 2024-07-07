class Solution:
    def addDigits(self, num: int) -> int:
        num_str = str(num)
        
        while len(num_str) > 1:
            res = 0
            for ch in num_str:
                res += int(ch)
            num_str = str(res)
            
        return int(num_str)