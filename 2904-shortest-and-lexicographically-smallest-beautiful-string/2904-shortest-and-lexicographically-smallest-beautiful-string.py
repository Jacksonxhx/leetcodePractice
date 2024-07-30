class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k:
            return ''
        
        res = s
        cnt = left = 0
        
        for right, c in enumerate(s):
            cnt += int(c)
            while cnt > k or s[left] == '0':
                cnt -= int(s[left])
                left += 1
            
            # k个1的情况
            if cnt == k:
                t = s[left : right + 1]
                if len(t) < len(res) or len(t) == len(res) and t < res:
                    res = t
        
        return res