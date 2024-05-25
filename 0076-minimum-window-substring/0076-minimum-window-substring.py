class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        维护一个快慢指针维护的滑动窗口
        维护一个哈希表，用来存储s中的substring出现t里字母的次数
        时刻更新最小的res
        '''
        if len(t) > len(s):
            return ""
        
        # 构建t的hash表
        hasht = Counter(t)
        count = len(t)
        
        left = 0
        min_len = float('inf')
        min_window = ""
        
        # 用滑动窗口在s中查找包含t所有字符的子串
        for right, char in enumerate(s):
            # 如果遇到一个t的字母，count--
            if hasht[char] > 0:
                count -= 1
            hasht[char] -= 1
            
            # 当count == 0，代表已经找到了对应的substring
            while count == 0:
                # 当当前substring是最小的情况时
                if right - left + 1 < min_len:
                    # 更新最小长度
                    min_len = right - left + 1
                    # 更新最小窗口
                    min_window = s[left:right + 1]
                
                # 调整 hasht 和 count，准备收缩窗口
                hasht[s[left]] += 1
                if hasht[s[left]] > 0:
                    count += 1
                left += 1
        
        return min_window