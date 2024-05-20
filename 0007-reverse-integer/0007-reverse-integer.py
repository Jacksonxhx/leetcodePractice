class Solution:
    def reverse(self, x: int) -> int:
        upper_limit, lower_limit = 1, -1
        i = 1
        while i <= 31:
            upper_limit *= 2
            lower_limit *= 2
            i += 1
        upper_limit -= 1
        
        is_negative = False
        if x < 0:
            is_negative = True
            x *= -1
            
        str_x = str(x)
        rev_x = str_x[::-1]
        res = int(rev_x)
        
        if res <= lower_limit or res >= upper_limit:
            return 0
        
        if is_negative:
            return -1 * res
        else:
            return res