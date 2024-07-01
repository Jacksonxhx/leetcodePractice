class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        length = len(columnTitle)
        for i in range(length):
            num = ord(columnTitle[i]) - ord('A') + 1
            res = res * 26 + num
        
        return res