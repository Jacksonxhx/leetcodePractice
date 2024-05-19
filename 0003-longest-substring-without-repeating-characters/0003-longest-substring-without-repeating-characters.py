class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        不定长度的sliding window快慢双指针
        用hash table记录个数
        '''
        l, r = 0, 0
        hasht = dict()
        ans = 0
        
        while r < len(s):
            # 在窗口加入字符
            if s[r] not in hasht:
                hasht[s[r]] = 1
            else:
                hasht[s[r]] += 1
            
            # 把window中重复的字符去掉为止
            while hasht[s[r]] > 1:
                hasht[s[l]] -= 1
                l += 1
            
            # ans取有过的最大的window size
            ans = max(ans, r - l + 1)
            r += 1
        
        return ans