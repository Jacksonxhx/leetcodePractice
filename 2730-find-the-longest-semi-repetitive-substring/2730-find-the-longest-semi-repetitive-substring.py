class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        """
        用一个cnt记录pair总数，然后i，j分别判断有没有pair，j有2个了i前进，i判断cnt--
        """
        i, j = 0, 0
        cnt, res = 0, 0
        n = len(s)
        
        while j < n:
            if cnt > 1:
                if s[i] == s[i + 1]:
                    cnt -= 1
                i += 1
            else:
                if j + 1 < n and s[j] == s[j + 1]:
                    cnt += 1
                j += 1
                
            res = max(res, j - i)
        
        return res