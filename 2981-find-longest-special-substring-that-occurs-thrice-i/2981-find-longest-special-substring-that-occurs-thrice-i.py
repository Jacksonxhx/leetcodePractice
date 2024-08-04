class Solution:
    def maximumLength(self, s: str) -> int:
        """
        find all substring and store in hash, find the longest
        """
        def is_special(ss: str) -> bool:
            return len(set(list(ss))) == 1
            
        hasht = dict()
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                s_tmp = s[i:j]
                if s_tmp not in hasht:
                    hasht[s_tmp] = 1
                else:
                    hasht[s_tmp] += 1
        res = -1
        for key, value in hasht.items():
            if value >= 3 and is_special(key):
                res = max(res, len(key))
        
        return res