class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        i, j = 0, 1
        s = list(s)
        
        res = 0
        while j < n:
            if s[i] != s[j]:
                res += 1
            i += 2
            j += 2
        
        return res