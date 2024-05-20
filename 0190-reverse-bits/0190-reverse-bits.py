class Solution:
    def reverseBits(self, n: int) -> int:
        str_n = bin(n)[2:]
        rev_str_n = str_n[::-1]
        while len(rev_str_n) < 32:
            rev_str_n += '0'
        
        return int(rev_str_n, 2)