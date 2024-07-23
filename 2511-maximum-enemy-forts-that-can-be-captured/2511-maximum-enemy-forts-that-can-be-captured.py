class Solution:
    def captureForts(self, forts: List[int]) -> int:
        i, j = 0, 0
        res = 0
        
        while j < len(forts) - 1:
            j += 1
            if forts[j] == -1 or forts[j] == 1:
                if forts[i] != 0 and forts[i] != forts[j]:
                    res = max(res, j - i - 1)
                i = j
        
        return res