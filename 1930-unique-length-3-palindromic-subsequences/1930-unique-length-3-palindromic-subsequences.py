class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        hasht存前后，减去一样的
        """
        hasht = defaultdict(list)
        for i, ch in enumerate(s):
            hasht[ch].append(i)
        
        res = 0
        
        for p in hasht:
            if len(hasht[p]) < 2:
                continue
            
            start, end = hasht[p][0], hasht[p][-1]
            res += len(set(s[start + 1:end]))
        
        return res