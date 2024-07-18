class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = len(s)
        
        # dp含义：s[0:i]是否可以拆分成单词，能存true，不能存false
        dp = [False] * (m + 1)
        dp[0] = True
        
        for i in range(m + 1):
            for j in range(i):
                # 当之前的[0:j]的字符串和从j到现在这个长度的字符串在wordDict，证明可以拆分
                if dp[j] and s[j : i] in wordDict:
                    # 则当前这个[0:i]的字符串是true
                    dp[i] = True
        
        return dp[m]