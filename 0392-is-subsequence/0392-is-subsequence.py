class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        #定义双指针
        i = 0
        j = 0
        
        #一个从subsequence走，一个从t走
        #当s[i] == t[j]时，i++
        #所以当i的值==s的size时，就代表有个subsequence
        while j < len(t):
            if i < len(s) and t[j] == s[i]:
                i += 1
            j += 1
        
        if i == len(s): return True
        else: False
        